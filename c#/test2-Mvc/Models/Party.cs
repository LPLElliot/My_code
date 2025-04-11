using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace PartyApp.Models
{
    public class Party
    {
        public int Id { get; set; }
        [Required]
        [Display(Name = "聚会主题")]
        public string Title { get; set; } = ""; // 初始化为 ""
        [Required]
        [Display(Name = "聚会地点")]
        public string Location { get; set; } = ""; // 初始化为 ""
        [Required]
        [Display(Name = "聚会时间")]
        public DateTime EventDate { get; set; }
        [Display(Name = "描述")]
        public string Description { get; set; } = ""; // 初始化为 ""
        public ICollection<Guest> Guests { get; set; } = new List<Guest>(); // 初始化为空列表
    }
}