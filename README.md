# Speech Translation System

This Python script allows users to translate spoken sentences from one language to another using the Google Cloud Speech-to-Text and Translation APIs. The translated text is then converted into speech and played back to the user.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- The required Python packages: `speech_recognition`, `googletrans`, and `gtts`.

You can install the required packages using pip:


## Usage

1. Run the script using Python:


2. Follow the on-screen instructions:
   - Speak 'hello' to initiate the translation.
   - Speak a sentence in English.
   - The script will translate the sentence to Hindi and play back the translated speech.

## Configuration

- You can change the source and target languages in the script by modifying the `from_lang` and `to_lang` variables in the `translate_speech()` function.
- Adjustments to the microphone sensitivity and ambient noise suppression can be made by changing the parameters in the `adjust_for_ambient_noise()` function.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the GNU General Public License v3.0 
### About the GNU General Public License (GPL)

The GNU General Public License (GPL) is a free, copyleft license for software and other kinds of works, which means that it permits the modification and redistribution of the software under the same license. The GPL license guarantees end users the freedom to run, study, share, and modify the software.

By using the GPL for this project, we ensure that all modifications and derivative works are also free and open source. If you distribute copies of or modifications to the project's source code, they must also be under the GPL or a compatible license.

For more information, please visit [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).

