---
title: V1 Acknowledgments
type: Frontmatter
volume: 1
chapter: 0
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/frontmatter/acknowledgements.qmd
source_anchor: acknowledgments
source_mode: Repository QMD
tags:
- Type/Frontmatter
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/frontmatter/acknowledgements.html
---

# V1 Acknowledgments

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^acknowledgments

## Origins

^origins

This book owes its existence to a single conversation. During a sabbatical at Google, Pete Warden invited me to work on what seemed like an impossible moonshot for TinyML: running a small speech model on a microcontroller. That collaboration on TensorFlow Lite for Microcontrollers revealed something fundamental. The constraints that govern a device with 16 KB to 256 KB of memory are the same constraints that govern an accelerator in a data center, even when the scale is entirely different. Bandwidth, latency, energy, and memory obey the same physics across both settings. That insight became the seed of this book.

The TinyML work led to an online course on HarvardX, co-taught with Laurence Moroney, that grew to over 100,000 students worldwide. Brian Plancher helped build the TinyML curriculum. Marcelo Rovai, a professor who first encountered the material through the TinyML course, went on to develop the hands-on labs and kits that accompany this book. Zach Shelby opened the Edge Impulse platform for student use. Massimo Banzi and the Arduino team, along with Eric Pan and Seeed Studio, collaborated with us in developing and providing the hardware kits that made hands-on instruction possible. Marco Zennaro brought the material to developing countries through ICTP and planted the idea that these principles deserved a proper textbook. Teaching at that scale, without one, made the need undeniable.

That need turned into a book through CS249r at Harvard University. In 2023, the semester-long class project was to write the class notes: each student group took ownership of a topic, researched it, and worked with me to develop it into a chapter. That work seeded every chapter in this book. The premise was that writing forces you to think more deeply than reading alone. We then opened it all on GitHub, and what began as rough class notes has been rewritten and refined with every semester since.

Because that GitHub work continues, this book benefits from a community whose contributions evolve with the project. New contributors join as readers report issues, improve explanations, and extend the supporting materials. A printed acknowledgment can capture only one moment in that continuing history. The current contributor list and contribution guidelines are available at <https://mlsysbook.ai/git>.

## Collaborators and Colleagues

^collaborators-and-colleagues

Beyond the class and GitHub community, my earlier collaborations shaped the book’s intellectual foundations. My time at Google informed much of the systems thinking in these pages. That period began with performance modeling for the first Pixel system on chip (SoC), drawing on my background in computer architecture. A collaboration with Mark Hill on roofline-style analytical modeling for heterogeneous SoCs taught me to reason about hardware from first principles, the kind of quantitative thinking that runs through every chapter. That emphasis on quantitative evaluation carried into my work on MLPerf. MLPerf involved many contributors across MLCommons, but I worked most closely with Peter Mattson, David Kanter, Carole-Jean Wu, Christine Cheng, Guenther Schmuelling, Cody Coleman, and Cliff Young. That collaboration shaped how I think about rigorous measurement of ML systems.

Boris Murmann and Song Han convinced me in the early stages that this project was worth pursuing. As I wrote, I sought feedback from colleagues in industry and academia alike. Practitioners at Arm, Google, Intel, Meta, Microsoft, Qualcomm, STMicroelectronics, and other organizations offered perspectives grounded in production systems, while academic reviewers at universities across Europe, Asia, and the Americas stress-tested the material against their own research and teaching. Their combined feedback sharpened every chapter. Evgeni Gousev at Qualcomm and Pete Bernard at the Edge AI Foundation supported the project’s outreach and helped build the community around it.

That feedback loop extended to classrooms around the world, where instructors put the material to the test when it was still rough. Sophia Shao at UC Berkeley, Xiaofan (Fred) Jiang at Columbia, Tushar Krishna and Divya Mahajan at Georgia Tech, and Wenkai Guan at the University of Minnesota Morris were among the first, and instructors at IIT Bombay, NUST Pakistan, De La Salle University in the Philippines, and universities across Europe, Latin America, and Africa have since adopted the book for their own courses. Their willingness to teach from an unfinished textbook provided invaluable feedback and confirmed that the need for this material was not limited to any one institution or any one country.

## Students and Contributors

^students-and-contributors

Closer to home, my students in the Edge Computing Lab at Harvard shaped this book in ways I cannot fully trace. Some did foundational work that helped establish TinyML as a field; their research and the ideas that emerged from years of collaboration informed the book’s technical content. This cohort helped set the field in motion and then helped me write about it: Andy Cheng, Arya Tschand, Brian Plancher, Colby Banbury, Elizabeth Suitor, Emma Chen, Ikechukwu Uchendu, Jason Jabbour, Jason Yik, Jeffrey Ma, Jessica Quaye, Mark Mazumder, Matthew Stewart, Maximilian Lam, Radhika Ghosal, Shvetank Prakash, Srivatsan Krishnan, Yu-Shun Hsiao, and Zishen Wan. Kai Kleinbard, then at the Harvard Extension School, built the online generative AI SocratiQ tutor bot. Naeem Khoshnevis, from the Harvard Kempner Institute, established essential infrastructure including GitHub Actions and documentation standards. Željko Hrček produced the TikZ diagrams and contributed to the PDF layout, page composition, and final visual formatting of the book.

I am also grateful to the researchers whose work this book builds on and to the open-source contributors worldwide who helped refine the manuscript, whether by fixing a single typo or by rewriting entire sections. The book improved because people who owed it nothing chose to make it better. What kept me going, aside from stubbornness, was that community: every GitHub star was a signal that someone out there cared, that someone was learning, that the work mattered. I am grateful to every one of them.

## Support

^support

This work also depended on support from the Harvard Data Science Initiative, Harvard Extension School, and the National Science Foundation, as well as from the Edge AI Foundation and ICTP for educational outreach and scholarships. Arduino, Edge Impulse, Google, and Seeed Studio provided hardware, tooling, and infrastructure that enabled the practical labs.

At MIT Press, Susan Hartman believed in this project and guided it from an open-source experiment to a published textbook. Her support, editorial judgment, and friendship made this book real in a way that GitHub alone could not. I am equally grateful to MIT Press for agreeing to keep this book available as open access. A textbook about a discipline shaped by the open-source community should be accessible to everyone in it. That MIT Press shared this conviction made all the difference.

Finally, I thank my wife, Kari, and my daughters, Nora and Maya. This book was written in the hours that belonged to them: late nights that started at ten and ended at two or three in the morning, weekends that disappeared into revisions, years of mornings when I was present but not quite there. The cost was real, and they paid it with patience I did not always deserve.

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/frontmatter/acknowledgements.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/frontmatter/acknowledgements.html#acknowledgments). Rendering provenance is recorded in the import manifest.
