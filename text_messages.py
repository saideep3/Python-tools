from twilio.rest import Client
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#comitted
driver = webdriver.Chrome()
driver.get("https://www.cricbuzz.com/live-cricket-scores/20303/aus-vs-ind-3rd-test-india-tour-of-australia-2018-19")
wait = WebDriverWait(driver, 20)

wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='matchCenter']/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/h2")))

driver.execute_script("window.stop();")
score = driver.find_element_by_xpath("//*[@id='matchCenter']/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/h2").text
print(score)
#driver.find_element_by_id("fwt-nav-button").click()
#
# Your Account SID from twilio.com/console
account_sid = "AC199ec814548391cc47a9571fc4742cfe"
# Your Auth Token from twilio.com/console
auth_token  = "2c8997b88b493fba7b7b6d2aa9391cd3"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918074038872",
    from_="+13365608850",
    body=score)

print(message.sid)