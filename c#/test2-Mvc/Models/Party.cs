using System.ComponentModel.DataAnnotations;

namespace PartyApp.Models
{
    public class Party
    {
        public int Id { get; set; }
        [Required]
        [Display(Name = "聚会主题")]
        public string Title { get; set; } = "";
        [Required]
        [Display(Name = "聚会地点")]
        public string Location { get; set; } = "";
        [Required]
        [Display(Name = "聚会时间")]
        public DateTime EventDate { get; set; }
        [Display(Name = "描述")]
        public string Description { get; set; } = "";
        public ICollection<Guest> Guests { get; set; } = new List<Guest>();
    }
}