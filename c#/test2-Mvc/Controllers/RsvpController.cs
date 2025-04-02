using Microsoft.AspNetCore.Mvc;
using System.Linq;
using test2_Mvc.Models;
using test2_Mvc.Data;

namespace test2_Mvc.Controllers
{
    public class RsvpController : Controller
    {
        private readonly AppDbContext _context;

        public RsvpController(AppDbContext context)
        {
            _context = context;
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Create(Rsvp rsvp)
        {
            if (ModelState.IsValid)
            {
                if (_context.Rsvps.Any(r => r.Email == rsvp.Email && r.PartyId == rsvp.PartyId))
                {
                    ModelState.AddModelError("Email", "该邮箱已登记本聚会");
                    return View(rsvp);
                }

                _context.Add(rsvp);
                _context.SaveChanges();
                return RedirectToAction("Confirmation", new { name = rsvp.Name, partyId = rsvp.PartyId });
            }
            return View(rsvp);
        }

        public IActionResult Confirmation(string name, int partyId)
        {
            ViewBag.Name = name;
            ViewBag.PartyId = partyId;
            return View();
        }
    }
}