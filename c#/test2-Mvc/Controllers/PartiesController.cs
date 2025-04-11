using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using PartyApp.Data;
using PartyApp.Models;
using System.Linq;
using System.Threading.Tasks;

namespace PartyApp.Controllers
{
    public class PartiesController : Controller
    {
        private readonly ApplicationDbContext _context;

        public PartiesController(ApplicationDbContext context)
        {
            _context = context;
        }

        public async Task<IActionResult> Index()
        {
            return _context.Parties != null ?
                        View(await _context.Parties.ToListAsync()) :
                        Problem("Entity set 'ApplicationDbContext.Parties'  is null.");
        }

        public async Task<IActionResult> Details(int? id)
        {
            if (id == null || _context.Parties == null)
            {
                return NotFound();
            }

            var party = await _context.Parties
                .FirstOrDefaultAsync(m => m.Id == id);
            if (party == null)
            {
                return NotFound();
            }

            var guests = await _context.Guests.Where(g => g.PartyId == party.Id).ToListAsync();
            var viewModel = new PartyGuestViewModel
            {
                Party = party,
                Guests = guests
            };

            return View(viewModel);
        }

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Title,Location,EventDate,Description")] Party party)
        {
            if (ModelState.IsValid)
            {
                _context.Add(party);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(party);
        }

        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null || _context.Parties == null)
            {
                return NotFound();
            }

            var party = await _context.Parties.FindAsync(id);
            if (party == null)
            {
                return NotFound();
            }
            return View(party);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Title,Location,EventDate,Description")] Party party)
        {
            if (id != party.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(party);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!PartyExists(party.Id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            return View(party);
        }

        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null || _context.Parties == null)
            {
                return NotFound();
            }

            var party = await _context.Parties
                .FirstOrDefaultAsync(m => m.Id == id);
            if (party == null)
            {
                return NotFound();
            }

            return View(party);
        }

        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (_context.Parties == null)
            {
                return Problem("Entity set 'ApplicationDbContext.Parties'  is null.");
            }
            var party = await _context.Parties.FindAsync(id);
            if (party != null)
            {
                _context.Parties.Remove(party);
            }

            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool PartyExists(int id)
        {
            return (_context.Parties?.Any(e => e.Id == id)).GetValueOrDefault();
        }

        [HttpPost]
        public async Task<IActionResult> Register(int partyId, string name, string email, string phone)
        {
            var existingGuest = await _context.Guests.FirstOrDefaultAsync(g => g.Email == email && g.PartyId == partyId);
            if (existingGuest != null)
            {
                ModelState.AddModelError("Email", "该邮箱已经注册过该聚会！");
                var party = await _context.Parties.FindAsync(partyId);
                if (party == null)
                {
                    return NotFound();
                }
                var guests = await _context.Guests.Where(g => g.PartyId == partyId).ToListAsync();
                var viewModel = new PartyGuestViewModel
                {
                    Party = party,
                    Guests = guests
                };
                return View("Details", viewModel);
            }

            var guest = new Guest
            {
                PartyId = partyId,
                Name = name,
                Email = email,
                Phone = phone
            };

            _context.Guests.Add(guest);
            await _context.SaveChangesAsync();

            return RedirectToAction("Confirmation", new { name = name, partyId = partyId });
        }

        // GET: Parties/Confirmation
        public IActionResult Confirmation(string name, int partyId)
        {
            ViewBag.Name = name;
            ViewBag.PartyId = partyId;
            return View();
        }

        // GET: Parties/ShowAttenders
        public async Task<IActionResult> ShowAttenders(int partyId)
        {
            var party = await _context.Parties.FindAsync(partyId);
            if (party == null)
            {
                return NotFound();
            }

            var guests = await _context.Guests.Where(g => g.PartyId == partyId).ToListAsync();
            var viewModel = new PartyGuestViewModel
            {
                Party = party,
                Guests = guests
            };

            return View(viewModel);
        }

        // GET: Parties/ShowUserParties
        public async Task<IActionResult> ShowUserParties(string email)
        {
            var guests = await _context.Guests.Where(g => g.Email == email).Include(g => g.Party).ToListAsync();
            return View(guests);
        }
    }
}