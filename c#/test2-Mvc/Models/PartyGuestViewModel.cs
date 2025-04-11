using System.Collections.Generic;

namespace PartyApp.Models
{
    public class PartyGuestViewModel
    {
        public Party Party { get; set; } = new Party(); //初始化
        public List<Guest> Guests { get; set; } = new List<Guest>(); //初始化
    }
}