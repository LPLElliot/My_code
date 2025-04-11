using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using PartyApp.Data;
using System.Diagnostics; // 添加此 using 指令
using test2_Mvc.Models;  //添加此using指令

namespace PartyApp.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly ApplicationDbContext _context;

        public HomeController(ILogger<HomeController> logger, ApplicationDbContext context)
        {
            _logger = logger;
            _context = context;
        }

        public async Task<IActionResult> Index()
        {
            var parties = await _context.Parties.ToListAsync();
            return View(parties);
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}