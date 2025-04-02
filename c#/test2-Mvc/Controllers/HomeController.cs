using Microsoft.AspNetCore.Mvc;
using test2_Mvc.Data;
using test2_Mvc.Models;
using System.Linq;
using Microsoft.EntityFrameworkCore;
public class HomeController : Controller
{
    private readonly AppDbContext _context;

    public HomeController(AppDbContext context)
    {
        _context = context;
    }

    public IActionResult Index()
    {
        return View(_context.Parties.ToList());
    }

    public IActionResult Attenders(int id)
    {
        var attenders = _context.Rsvps
            .Where(r => r.PartyId == id)
            .Include(r => r.Party)
            .ToList();
        return View(attenders);
    }
}