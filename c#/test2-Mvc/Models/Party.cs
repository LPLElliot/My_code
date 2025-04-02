using System.ComponentModel.DataAnnotations;

namespace test2_Mvc.Models
{
    public class Party
    {
        public int Id { get; set; }
        [Required]
        public string? Name { get; set; }
        [Display(Name = "Location")]
        public string? Location { get; set; }
        [DataType(DataType.Date)]
        public DateTime Date { get; set; }
    }
}