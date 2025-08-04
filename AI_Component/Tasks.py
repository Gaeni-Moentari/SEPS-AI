from crewai import Task
from AI_Component.Agents import *
from AI_Component.Tools import *


agents = Agents()

class Tasks:
    def __init__(self, input, lang):
        self.input=input
        self.lang=lang
    
    def general_search_task(self):
        return Task(
            description=f"Tugas kamu adalah mencari dan mengumpulkan informasi terkait SEAMEO SEPS berdasarkan input {self.input}, termasuk data, program, kegiatan, serta kebijakan yang relevan. "
                         "Berikan hasil pencarian yang mencakup ringkasan informasi dari berbagai sumber serta link referensinya. "
                         "Gunakan tools[WebSearch] untuk mendapatkan informasi yang akurat dan terkini."
                         "Gunakan referensi link berikut ini : "
                         "https://www.seameoseps.org/"
                         "https://www.seameo.org/"
                         "dan link lainnya seperti media, web, dan banyak lagi",
            expected_output="sebuah hasil pencarian yang lengkap dari berbagai sumber dengan link sumber nya"
                            " gunakan format yang mudah dipahami untuk bahan menyusun jawaban yang komprehensif",
            agent=agents.data_search(),
            tools=[WebSearch]
        )
    
    def general_answer_task(self):
        return Task(
            description="Tugas kamu adalah :"
                        f"Menjawab pertanyaan berikut terkai SEAMEO SEPS : {self.input}"
                        "gunakan data yang telah dicari sebelumnya untuk memberikan jawaban yang akurat dan relevan."
                        "sematkan link referensi yang mendukung jawabanmu dari informasi yang tersedia",
            expected_output="Jawaban dibuat dengan markdown dengan format seperti wikipedia singkat"
                            "Jawaban menyertakan referensi yang bisa dikunjungi di akhir"
                            f"jawaban HARUS Menggunakan bahasa berikut = {self.lang}",
            agent=agents.general_answer()
        )