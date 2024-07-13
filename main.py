from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from time import time
from os.path import exists
from os import mkdir, listdir


class PhotoAlbumApp(App):
    image_list = []
    def build(self):
        return Builder.load_file("photo.kv")

    def take_picture(self, camera):
        if not exists("album"):
            mkdir("album")
        print("taking picture")
        camera.export_to_png(f"album/IMG{int(time())}.png")

    def create_album(self, grid):
        """
        always clears images from grid and add them again
        set `on_leave: grid.clear_widgets()`
        :param grid:
        :return:
        """
        for image_name in listdir("album"):
            grid.add_widget(
                Image(
                    source=f"album/{image_name}"
                )
            )

    def create_album2(self, grid):
        """
        remembers previous added images to be able to continue
        from recent added images
        :param grid:
        :return:
        """
        for image_name in listdir("album"):
            if image_name in self.image_list:
                continue
            grid.add_widget(
                Image(
                    source=f"album/{image_name}"
                )
            )
            self.image_list.append(image_name)


if __name__ == "__main__":
    PhotoAlbumApp().run()