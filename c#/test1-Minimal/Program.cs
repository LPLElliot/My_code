using MinimalApiApp.Models;
using MinimalApiApp.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSingleton<PartyService>();

var app = builder.Build();

app.UseHttpsRedirection();

// 获取所有聚会信息
app.MapGet("/Party/All", (PartyService partyService) => partyService.GetAllParties());

// 按 ID 获取特定聚会信息
app.MapGet("/Party/{id}", (int id, PartyService partyService) =>
{
    var party = partyService.GetPartyById(id);
    return party is null ? Results.NotFound() : Results.Ok(party);
});

// 添加新聚会
app.MapPost("/Party", (Party party, PartyService partyService) =>
{
    var createdParty = partyService.AddParty(party);
    return Results.Created($"/Party/{createdParty.Id}", createdParty);
});

// 按 ID 更新特定聚会信息
app.MapPut("/Party/{id}", (int id, Party updatedParty, PartyService partyService) =>
{
    var result = partyService.UpdateParty(id, updatedParty);
    return result ? Results.NoContent() : Results.NotFound();
});

// 按 ID 删除特定聚会
app.MapDelete("/Party/{id}", (int id, PartyService partyService) =>
{
    var result = partyService.DeleteParty(id);
    return result ? Results.Ok() : Results.NotFound();
});

app.Run();
