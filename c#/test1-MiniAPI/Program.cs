namespace test1_MiniAPI
{
    public class Party
    {
        public int Id { get; set; }
        public string? Topic { get; set; }
        public string? Location { get; set; }
        public DateTime Time { get; set; }
    }

    public class PartyService
    {
        private readonly List<Party> _parties = new();
        private int _nextId = 1;

        public IEnumerable<Party> GetAllParties()
        {
            return _parties;
        }

        public Party? GetPartyById(int id)
        {
            return _parties.FirstOrDefault(p => p.Id == id);
        }

        public Party AddParty(Party party)
        {
            party.Id = _nextId++;
            _parties.Add(party);
            return party;
        }

        public bool UpdateParty(int id, Party updatedParty)
        {
            var party = GetPartyById(id);
            if (party == null)
            {
                return false;
            }
            party.Topic = updatedParty.Topic;
            party.Location = updatedParty.Location;
            party.Time = updatedParty.Time;
            return true;
        }

        public bool DeleteParty(int id)
        {
            var party = GetPartyById(id);
            if (party == null)
            {
                return false;
            }
            _parties.Remove(party);
            return true;
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);
            builder.Services.AddSingleton<PartyService>();

            var app = builder.Build();

            app.MapGet("/Party/All", (PartyService partyService) =>
            {
                return partyService.GetAllParties();
            });

            app.MapGet("/Party/{id}", (int id, PartyService partyService) =>
            {
                var party = partyService.GetPartyById(id);
                if (party == null)
                {
                    return Results.NotFound();
                }
                return Results.Ok(party);
            });

            app.MapPost("/Party", (Party party, PartyService partyService) =>
            {
                var newParty = partyService.AddParty(party);
                return Results.Created($"/Party/{newParty.Id}", newParty);
            });

            app.MapPut("/Party/{id}", (int id, Party updatedParty, PartyService partyService) =>
            {
                var result = partyService.UpdateParty(id, updatedParty);
                if (!result)
                {
                    return Results.NotFound();
                }
                return Results.NoContent();
            });

            app.MapDelete("/Party/{id}", (int id, PartyService partyService) =>
            {
                var result = partyService.DeleteParty(id);
                if (!result)
                {
                    return Results.NotFound();
                }
                return Results.NoContent();
            });

            app.Run();
        }
    }
}