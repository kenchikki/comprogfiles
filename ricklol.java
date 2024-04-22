import java.awt.Desktop;
import java.net.URI;

public class Rickroll {
    public static void main(String[] args) {
        try {
            // Open the browser to the Rick Astley song
            Desktop.getDesktop().browse(new URI("https://www.youtube.com/watch?v=dQw4w9WgXcQ"));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

