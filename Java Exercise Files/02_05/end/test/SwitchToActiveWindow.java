import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class SwitchToActiveWindow {
    public static void main(String[] args) {

        System.setProperty("webdriver.chrome.driver", "/Users/meaghanlewis/Downloads/chromedriver");

        WebDriver driver = new ChromeDriver();

        driver.get("https://formy-project.herokuapp.com/switch-window");

        WebElement newTabButton = driver.findElement(By.id("new-tab-button"));
        newTabButton.click();

        String originalHandle = driver.getWindowHandle(); // at this point, the driver will focus on the current window(tab), after clicking the new tab button. So this will get the window handle ID and stores in new webelement.



        for(String handle1: driver.getWindowHandles()) { //a loop that will switch to the second tap that is open in the browser.
            driver.switchTo().window(handle1); 
        }

        driver.switchTo().window(originalHandle); //this will switch back to the original tab, that was the main focus of the webdriver.

        driver.quit();
    }
}
