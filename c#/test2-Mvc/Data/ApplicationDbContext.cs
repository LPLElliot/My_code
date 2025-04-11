using Microsoft.EntityFrameworkCore;
using PartyApp.Models;

namespace PartyApp.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
        {
        }

        public DbSet<Party> Parties { get; set; }
        public DbSet<Guest> Guests { get; set; }
    }
}