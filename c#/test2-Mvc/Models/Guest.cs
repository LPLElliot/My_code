using System.ComponentModel.DataAnnotations;

namespace PartyApp.Models
{
    public class Guest
    {
        public int Id { get; set; }
        [Required]
        [Display(Name = "姓名")]
        public string Name { get; set; } = ""; // 初始化为 ""
        [Required]
        [EmailAddress]
        [Display(Name = "邮箱")]
        public string Email { get; set; } = ""; // 初始化为 ""
        [Display(Name = "电话")]
        public string Phone { get; set; } = ""; // 初始化为 ""
        public int PartyId { get; set; }
        public Party Party { get; set; } = new Party(); //初始化
    }
}