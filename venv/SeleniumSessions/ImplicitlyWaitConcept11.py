from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

#default value of Implicitly wait is zero
driver.implicitly_wait(10)
# --> title issue cannot be handled using implicitly wait


# time out = 10
# dynamic wait
# imp wait will be applied for all the we elements available on the page
# global wait
# whenever u use find_element and find_elements method
# only for web elements (not for tile or url.. in that case we use explicitly wait)
# hubspot title is not handled using implicitly wait

driver.get('https://app.hubspot.com/login?hubs_signup-url=www.hubspot.com/&hubs_signup-cta=homepage-nav-login&_ga=2.64166504.633728753.1624305769-86624004.1624305769&__cf_chl_jschl_tk__=ae909cf92dfe4dab300d094184c4d5fab64866b0-1624305772-0-AV9jnqxzfSZg2It9GEv0gRpnwA-hGo38SSLg3hRo7pzpIgi5yfGNFR_y5EOSxDjNmo6D9Rg4oBxtKLf9EvNZKzt2kg0ulIhG86D8us-gUhOMvZdCk4zsGx6KipadbMgzjlPnlRr6X0Ag2o1JCmP3lUQO1w5-4v9NTRs0Anr72tlZETvflGl9_TW28e7tsY6MmUjw3N1jO_9n5pBtGPwCsHbTfPvZVSJP_FYGkvyHXRi5qRtXvxNrkDzEyVetZYPEgjKgr5ZuQepXb-CuBQ9TWdMH94qV4KbdTVvu6EdpJt6CKdGPGIUinFMeh3z0St1r1spY9nVmrFe2fR8k9NefHsUc_kC6JMAzyOp-ScVhnkPlBLRUTPSp4enx1DM9xymHXAgHOizLAHlFVhYEc9ciZ2Gc2Ek3OZ4aUQCAzxZwnGF2DeWQQkU0lqMGacmwv_c67lS7wwN47n8yLtDCx11J0iaJc1trYTgnq0MYz-d-8dVxFeNdDN_uL_BRVrqJjvEoOjDDCBFLx-rcqYYkpotaS4pOb70h_EgVEnjnpH4y-d-ThJvQsmY9Y9Mxl8ztSORzzGuQh7yDJEvEw4_xuGwO4Zd34z0_R1IvyUDBXGPMz24-23M2gcs8edEw3ewuIH8iCQ')

user_name = driver.find_element(By.ID, 'username')
user_name.send_keys("test@gmail.com")

driver.find_element(By.ID, 'password').send_keys("test@12345")
# element3
# e4
# e5
# implicitly wait will be applied to all the elements



