using Microsoft.EntityFrameworkCore;
using test2_Mvc.Models;

namespace test2_Mvc.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
        {
        }

        public DbSet<Party> Parties { get; set; }
        public DbSet<Rsvp> Rsvps { get; set; }
    }
}