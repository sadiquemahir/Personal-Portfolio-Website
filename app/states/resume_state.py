import reflex as rx
from typing import TypedDict


class SocialLink(TypedDict):
    platform: str
    url: str
    icon: str


class SkillCategory(TypedDict):
    name: str
    skills: list[str]


class Experience(TypedDict):
    role: str
    company: str
    duration: str
    location: str
    description: list[str]


class Education(TypedDict):
    degree: str
    institution: str
    year: str
    location: str
    coursework: str


class Project(TypedDict):
    title: str
    description: str
    image: str
    icon: str
    technologies: list[str]
    github_url: str
    demo_url: str
    categories: list[str]


class Certificate(TypedDict):
    title: str
    issuer: str
    date: str
    icon: str


class TechStackItem(TypedDict):
    name: str
    icon: str
    category: str
    color: str


class ResumeState(rx.State):
    name: str = "Mahir Sadique"
    title: str = "Software Engineer"
    summary: str = "Motivated Software Engineer with strong experience across full-stack development, backend systems, and modern frontend frameworks. Skilled in building scalable applications, optimizing workflows, and delivering reliable solutions through clean code and strong problem-solving."
    email: str = "Sadiquemahir@gmail.com"
    phone: str = "267-212-6972"
    location: str = "Hatfield, Pennsylvania"
    active_tab: str = "Projects"
    portfolio_tabs: list[str] = ["Projects", "Certificates", "Tech Stack"]
    social_links: list[SocialLink] = [
        {"platform": "GitHub", "url": "https://github.com", "icon": "github"},
        {"platform": "LinkedIn", "url": "https://linkedin.com", "icon": "linkedin"},
        {"platform": "Email", "url": "mailto:Sadiquemahir@gmail.com", "icon": "mail"},
    ]
    skills_categories: list[SkillCategory] = [
        {
            "name": "Languages",
            "skills": [
                "Python",
                "Java",
                "C++",
                "SQL",
                "Rust",
                "Selenium",
                "TypeScript",
                "Svelte",
                "MATLAB",
                "JSON",
                "CSS",
                "React",
                "HTML",
                "MongoDB",
                "JavaScript",
                "Redis",
            ],
        },
        {
            "name": "Tools & Environments",
            "skills": [
                "Flask",
                "APIs",
                "XAMPP",
                "Pandas",
                "Matplotlib",
                "Git",
                "Docker",
                "SvelteKit",
                "Visual Studio",
                "MySQL",
                "Linux/Ubuntu",
                "Vector Database",
                "Django",
                "YOLO",
                "Swarm Intelligence",
                "ROS2 Jazzy",
            ],
        },
    ]
    experience: list[Experience] = [
        {
            "role": "Software Developer Intern",
            "company": "Paracosmos Studio Inc.",
            "duration": "January 2025 - May 2025",
            "location": "New York, NY",
            "description": [
                "Worked on TOME, a collaborative genealogy web app built with SvelteKit, by developing and executing end-to-end and unit tests using Selenium.",
                "Tested critical workflows such as user registration, login, and verification across frontend and backend components.",
                "Assisted in setting up and running the full-stack environment locally using Docker, Postgres, and MinIO.",
                "Gained hands-on experience with TypeScript, HTML/CSS, and environment configuration in a modern SvelteKit project.",
            ],
        }
    ]
    education: list[Education] = [
        {
            "degree": "B.S. in Computer Science",
            "institution": "The Pennsylvania State University",
            "year": "Received May 2025",
            "location": "University Park, PA",
            "coursework": "OOP With Web, Database Design, Computer Organization and Architecture, Data Structures, Machine Learning, Artificial Intelligence",
        }
    ]
    projects: list[Project] = [
        {
            "title": "TurtleBot Swarm Intelligence",
            "description": "Built an autonomous multi-robot search & rescue system using TurtleBot3, Raspberry Pi 4, and OpenCR, developed with Python 3.11 in the ROS2 Jazzy framework on Ubuntu 24.04. Used YOLO and LiDAR for real-time object detection and obstacle avoidance. Designed asyncio AI agents using asyncio for asynchronous inter-robot communication. Integrated AprilTags for localization and MongoDB/Redis for real-time data logging and sharing. Secured communication with HMAC and SSH, and managed code with GitHub and CI practices. Developed a ReactJS dashboard to monitor live missions, featuring a 2D Bot Location Map with directional tracking and Battery Monitoring for voltage and charge status, using MongoDB to fetch live mission data.",
            "image": "/placeholder.svg",
            "icon": "bot",
            "technologies": [
                "Python 3.11",
                "ROS2 Jazzy",
                "TurtleBot3",
                "Raspberry Pi 4",
                "OpenCR",
                "YOLO",
                "LiDAR",
                "asyncio",
                "AprilTags",
                "MongoDB",
                "Redis",
                "HMAC",
                "SSH",
                "ReactJS",
                "GitHub",
                "CI",
                "Ubuntu 24.04",
            ],
            "github_url": "https://github.com",
            "demo_url": "https://demo.com",
            "categories": ["Robotics", "AI", "Full Stack"],
        }
    ]
    certificates: list[Certificate] = [
        {
            "title": "B.S. in Computer Science",
            "issuer": "The Pennsylvania State University",
            "date": "May 2025",
            "icon": "graduation-cap",
        }
    ]
    project_categories: list[str] = ["All", "Robotics", "AI", "Full Stack"]
    selected_category: str = "All"
    is_loading: bool = False

    @rx.event
    def set_category(self, category: str):
        self.selected_category = category

    @rx.event
    def set_tab(self, tab: str):
        self.active_tab = tab

    @rx.var
    def filtered_projects(self) -> list[Project]:
        if self.selected_category == "All":
            return self.projects
        return [p for p in self.projects if self.selected_category in p["categories"]]

    @rx.var
    def tech_stack_items(self) -> list[TechStackItem]:
        items = []
        color_map = {
            "Python": "text-blue-400",
            "Java": "text-orange-500",
            "C++": "text-blue-600",
            "SQL": "text-purple-400",
            "Rust": "text-orange-600",
            "Selenium": "text-green-500",
            "TypeScript": "text-blue-500",
            "Svelte": "text-orange-500",
            "MATLAB": "text-orange-600",
            "JSON": "text-gray-400",
            "CSS": "text-blue-400",
            "React": "text-cyan-400",
            "HTML": "text-orange-500",
            "MongoDB": "text-green-500",
            "JavaScript": "text-yellow-400",
            "Redis": "text-red-500",
            "Flask": "text-gray-300",
            "APIs": "text-gray-300",
            "XAMPP": "text-orange-400",
            "Pandas": "text-purple-500",
            "Matplotlib": "text-blue-400",
            "Git": "text-orange-500",
            "Docker": "text-blue-500",
            "SvelteKit": "text-orange-500",
            "Visual Studio": "text-purple-500",
            "MySQL": "text-blue-500",
            "Linux/Ubuntu": "text-orange-500",
            "Vector Database": "text-purple-400",
            "Django": "text-green-600",
            "YOLO": "text-blue-500",
            "Swarm Intelligence": "text-purple-400",
            "ROS2 Jazzy": "text-blue-500",
            "AI": "text-purple-500",
        }
        for category in self.skills_categories:
            cat_name = category["name"]
            for skill in category["skills"]:
                icon = "code"
                if skill in [
                    "Python",
                    "Java",
                    "C++",
                    "Rust",
                    "TypeScript",
                    "JavaScript",
                ]:
                    icon = "file-code"
                elif skill in ["SQL", "MongoDB", "Redis", "MySQL", "Vector Database"]:
                    icon = "database"
                elif skill in ["React", "Svelte", "SvelteKit", "HTML", "CSS"]:
                    icon = "layout"
                elif skill in ["Docker", "Linux/Ubuntu", "Git"]:
                    icon = "terminal"
                elif skill in ["YOLO", "Swarm Intelligence", "ROS2 Jazzy", "AI"]:
                    icon = "brain"
                color = color_map.get(skill, "text-indigo-400")
                items.append(
                    {"name": skill, "icon": icon, "category": cat_name, "color": color}
                )
        return items

    @rx.event
    async def load_resume_data(self):
        """
        Simulates parsing the Resume.pdf file.
        In a real production app, this would use a library like pypdf to read
        assets/Resume.pdf and extract text using regex or NLP.
        """
        self.is_loading = True
        import asyncio

        await asyncio.sleep(0.5)
        self.is_loading = False

    @rx.event
    def download_resume(self):
        """
        Handles the resume download.
        """
        return rx.download(url="/Resume.pdf", filename="Mahir_Sadique_Resume.pdf")