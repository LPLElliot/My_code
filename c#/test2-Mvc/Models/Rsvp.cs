using System.ComponentModel.DataAnnotations;

namespace test2_Mvc.Models
{
    public class Rsvp
    {
        public int Id { get; set; }
        [Required]
        public string? Name { get; set; }
        [EmailAddress]
        public string? Email { get; set; }
        [Phone]
        public string? Phone { get; set; }
        public int PartyId { get; set; }
        public Party? Party { get; set; }
    }
}