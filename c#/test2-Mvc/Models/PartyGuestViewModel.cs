namespace PartyApp.Models
{
    public class PartyGuestViewModel
    {
        public Party Party { get; set; } = new Party();
        public List<Guest> Guests { get; set; } = new List<Guest>();
    }
}