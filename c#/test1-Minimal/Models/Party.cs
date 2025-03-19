namespace MinimalApiApp.Models;

public class Party
{
    // 聚会的唯一标识符
    public int Id { get; set; }
    
    // 聚会的主题
    public string? Topic { get; set; }
    
    // 聚会的地点
    public string? Location { get; set; }
    
    // 聚会的时间
    public DateTime Time { get; set; }
}