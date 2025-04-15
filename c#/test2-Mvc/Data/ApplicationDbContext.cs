using Microsoft.EntityFrameworkCore;
using PartyApp.Models;

namespace PartyApp.Data
{
    public class ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : DbContext(options)
    {
        public DbSet<Party> Parties { get; set; }
        public DbSet<Guest> Guests { get; set; }
    }
}