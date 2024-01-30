import argparse
from PIL import Image, ImageDraw, ImageFont, ImageSequence
from io import BytesIO

def generate_frames_with_text(width, height, text, n_frames=10):
    frames = []
    font_size = height / 10
    for i in range(n_frames):
        new_im = Image.new("RGB", (width, height), color=(255, 255, 255))

        # modify pixel 0,0 to be white.
        if i % 2 == 0:
            new_im.putpixel((0, 0), (0, 0, 0))

        font = ImageFont.truetype("Roboto-Regular.ttf", font_size)

        draw = ImageDraw.Draw(new_im)
        text_width = draw.textlength(text, font)

        if text_width < width:

            draw.text((5, (height - font_size)/2), text, font=font, fill=(0, 0, 0))
            frames.append(new_im)
            continue
        else:
            words = text.split(" ")
            lines = []
            line = ""
            for word in words:
                temp_line = line + word + " "
                temp_line_width = draw.textlength(temp_line, font)
                if temp_line_width < width:
                    line = temp_line
                else:
                    lines.append(line)
                    line = word + " "

            lines.append(line)
            y = (height - font_size * len(lines))/2
            for line in lines:
                draw.text((5, y), line, font=font, fill=(0, 0, 0))
                y += font_size

            frames.append(new_im)
            continue

    return frames

def calc_text_frames_n(frame_duration, text):
    # approx 4 words per second, add 2 seconds every time
    read_time_ms = (len(text.split(" ")) / 4 + 2) * 1000
    return int(read_time_ms / frame_duration)


def main():
    parser = argparse.ArgumentParser(description='Process a file.')
    parser.add_argument('path', type=str, help='Path to input gif. Text will be added before the gif.')
    parser.add_argument('text', type=str, help="Text to add to the gif.")

    args = parser.parse_args()

    if args.path is None or args.path.split(".")[-1] != "gif":
        print("Please specify a valid gif file.")
        return

    if args.text is None:
        print("Please specify text to be added.")
        return

    try:
        input_gif = Image.open(args.path)
    except FileNotFoundError:
        print("Gif file not found")
        return

    width, height = input_gif.size

    duration = ImageSequence.Iterator(input_gif)[0].info['duration']

    text_frames_n = calc_text_frames_n(duration, args.text)

    frames = generate_frames_with_text(height=height, width=width, text=args.text, n_frames=text_frames_n)

    temp_buffer = BytesIO()
    frames[0].save(temp_buffer, format='GIF', save_all=True, append_images=frames[1:], duration=100, loop=0)

    temp_buffer.seek(0)
    text_gif = Image.open(temp_buffer)

    combined = [text_gif, input_gif]

    output_filename = "pbt_" + args.path

    combined[0].save(output_filename, save_all=True, append_images=combined[1:], duration=100, loop=0)


if __name__ == "__main__":
    main()
