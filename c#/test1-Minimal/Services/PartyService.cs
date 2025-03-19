using MinimalApiApp.Models;

namespace MinimalApiApp.Services;

public class PartyService
{
    // 用于存储聚会信息的列表
    private readonly List<Party> _parties = new List<Party>();
    private int _nextId = 1;

    // 获取所有聚会信息
    public IEnumerable<Party> GetAllParties()
    {
        return _parties;
    }

    // 按 ID 获取特定聚会信息
    public Party? GetPartyById(int id)
    {
        return _parties.FirstOrDefault(p => p.Id == id);
    }

    // 添加新聚会
    public Party AddParty(Party party)
    {
        party.Id = _nextId++;
        _parties.Add(party);
        return party;
    }

    // 按 ID 更新特定聚会信息
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

    // 按 ID 删除特定聚会
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