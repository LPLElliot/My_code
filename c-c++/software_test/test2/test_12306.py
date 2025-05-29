import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime, timedelta

class Test12306TicketQuery(unittest.TestCase):
    def setUp(self):
        # 初始化Edge浏览器驱动
        edge_driver_path = EdgeChromiumDriverManager().install()
        options = Options()
        options.add_argument('--log-level=3') 
        service = Service(executable_path=edge_driver_path, log_path='NUL')
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = "https://www.12306.cn/index/"

    def tearDown(self):
        # 关闭浏览器
        self.driver.quit()

    def test_12306_ticket_query(self):
        # 打开12306首页
        self.driver.get(self.base_url)
        self.wait.until(EC.presence_of_element_located((By.ID, "fromStationText")))

        # 输入出发地
        from_city = self.driver.find_element(By.ID, "fromStationText")
        from_city.click()
        from_city.clear()
        from_city.send_keys("南京南")
        input("请手动点击下拉中的‘南京南’，选中后按回车继续...")

        # 输入目的地
        to_city = self.driver.find_element(By.ID, "toStationText")
        to_city.click()
        to_city.clear()
        to_city.send_keys("上海虹桥")
        input("请手动点击下拉中的‘上海虹桥’，选中后按回车继续...")

        # 选择出发日期（第二天）
        tomorrow = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        date_input = self.driver.find_element(By.ID, "train_date")
        date_input.clear()
        date_input.send_keys(tomorrow)

        # 点击查询按钮
        old_handles = self.driver.window_handles
        self.driver.find_element(By.ID, "search_one").click()

        # 等待新窗口出现并切换
        self.wait.until(lambda d: len(d.window_handles) > len(old_handles))
        new_handles = self.driver.window_handles
        for handle in new_handles:
            if handle not in old_handles:
                self.driver.switch_to.window(handle)
                break

        # 任务2：人工筛选
        input("请依次手动点击：‘智能动车组’、‘南京南’出发站、‘上海虹桥’到达站、发车时间‘12:00--18:00’，全部筛选后按回车继续...")

        # 任务3：提取所有车次信息
        train_rows = [
            tr for tr in self.driver.find_elements(By.CSS_SELECTOR, '#queryLeftTable > tr')
            if tr.is_displayed()
        ]
        count = len(train_rows)
        print(f"查询到的车次数量：{count}")

        trains = []
        min_duration = None
        for row in train_rows:
            try:
                # 车次号
                train_no = row.find_element(By.CSS_SELECTOR, '.train .number').text.strip()
                # 出发站和到达站
                cdz = row.find_elements(By.CSS_SELECTOR, '.cdz')
                if not cdz:
                    continue
                cdz = cdz[0]
                strongs = cdz.find_elements(By.TAG_NAME, 'strong')
                if len(strongs) < 2:
                    continue
                from_station = strongs[0].text.strip()
                to_station = strongs[1].text.strip()
                # 出发时间和到达时间
                cds = row.find_elements(By.CSS_SELECTOR, '.cds')
                if not cds:
                    continue
                cds = cds[0]
                start_time_elem = cds.find_elements(By.CSS_SELECTOR, '.start-t')
                end_time_elem = cds.find_elements(By.CSS_SELECTOR, '.color999')
                if not (start_time_elem and end_time_elem):
                    continue
                start_time = start_time_elem[0].text.strip()
                end_time = end_time_elem[0].text.strip()
                # 历时
                ls_elem = row.find_elements(By.CSS_SELECTOR, '.ls strong')
                if not ls_elem:
                    continue
                duration = ls_elem[0].text.strip()
                # 解析历时为分钟
                if ':' in duration:
                    hours, minutes = map(int, duration.split(':'))
                    total_minutes = hours * 60 + minutes
                else:
                    continue
                trains.append({
                    'train_no': train_no,
                    'from_station': from_station,
                    'to_station': to_station,
                    'start_time': start_time,
                    'end_time': end_time,
                    'duration': duration,
                    'total_minutes': total_minutes
                })
                if min_duration is None or total_minutes < min_duration:
                    min_duration = total_minutes
            except Exception as e:
                print("解析异常：", e)
                continue

        # 输出所有车次信息
        for t in trains:
            print(
                f"车次：{t['train_no']}，出发站：{t['from_station']}，到达站：{t['to_station']}，"
                f"出发时间：{t['start_time']}，到达时间：{t['end_time']}，历时：{t['duration']}"
            )

        # 输出历时最短的车次
        shortest_trains = [t for t in trains if t['total_minutes'] == min_duration]
        print("历时最短的车次：")
        for t in shortest_trains:
            print(
                f"{t['train_no']} 出发时间：{t['start_time']}，到达时间：{t['end_time']}，历时：{t['duration']}"
            )

        # 断言：筛选后应有车次，且存在历时最短的车次，历时格式正确
        self.assertGreater(count, 0, "筛选后应有车次")
        self.assertTrue(len(shortest_trains) > 0, "应存在历时最短的车次")
        for t in shortest_trains:
            self.assertIn(":", t['duration'], "历时格式应为hh:mm")

if __name__ == "__main__":
    unittest.main()