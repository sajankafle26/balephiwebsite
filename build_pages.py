#!/usr/bin/env python3
"""Build multi-page Balephi Energy website with proper nav and content."""

# ─── SHARED COMPONENTS ───

HEAD = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Balephi Energy Pvt. Ltd.</title>
    <meta name="description" content="Balephi Energy Pvt. Ltd. - Developing the 40MW Balephi Khola Hydroelectric Project in Sindhupalchowk, Nepal.">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        primary: '#dc2626',
                        primaryLight: '#ef4444',
                        secondary: '#1e3a8a',
                        dark: '#0f172a',
                        lightBg: '#f8fafc'
                    }},
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                        heading: ['Poppins', 'sans-serif'],
                    }},
                    boxShadow: {{
                        'soft': '0 10px 40px -10px rgba(0,0,0,0.08)',
                    }}
                }}
            }}
        }}
    </script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; }}
        h1,h2,h3,h4,h5,h6 {{ font-family: 'Poppins', sans-serif; }}
        ::-webkit-scrollbar {{ width: 8px; }}
        ::-webkit-scrollbar-track {{ background: #f1f1f1; }}
        ::-webkit-scrollbar-thumb {{ background: #dc2626; border-radius: 4px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: #b91c1c; }}
        .hero-overlay {{
            background: linear-gradient(to right, rgba(15,23,42,0.9) 0%, rgba(15,23,42,0.6) 50%, rgba(15,23,42,0.2) 100%);
        }}
        .nav-link {{ position: relative; padding-bottom: 0.5rem; }}
        .nav-link::after {{
            content: ''; position: absolute; bottom: 0; left: 0; width: 0; height: 2px;
            background-color: #dc2626; transition: width 0.3s ease;
        }}
        .nav-link:hover::after {{ width: 100%; }}
        .dropdown-menu {{
            display: none; position: absolute; top: 100%; left: 0; background-color: white;
            min-width: 280px; box-shadow: 0 10px 40px rgba(0,0,0,0.12); border-radius: 0.75rem;
            z-index: 50; padding: 0.5rem 0; border: 1px solid #f1f5f9;
            transform: translateY(8px); opacity: 0;
            transition: opacity 0.2s ease, transform 0.2s ease;
        }}
        .nav-dropdown:hover .dropdown-menu {{
            display: block; transform: translateY(0); opacity: 1;
            animation: fadeIn 0.25s ease forwards;
        }}
        .dropdown-item {{
            display: flex; align-items: center; padding: 0.7rem 1.25rem; color: #475569;
            font-size: 0.875rem; transition: all 0.2s; border-left: 3px solid transparent;
        }}
        .dropdown-item:hover {{
            background-color: #fef2f2; color: #dc2626; border-left-color: #dc2626;
        }}
        .dropdown-item i {{ width: 20px; margin-right: 0.75rem; font-size: 0.75rem; color: #94a3b8; transition: color 0.2s; }}
        .dropdown-item:hover i {{ color: #dc2626; }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(8px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
</head>
<body class="bg-lightBg text-slate-700 antialiased selection:bg-primaryLight selection:text-white">
"""

HEADER = """
    <!-- Top Bar -->
    <div class="bg-dark text-slate-300 py-2.5 text-sm border-b border-slate-800 hidden md:block">
        <div class="container mx-auto px-4 md:px-8 flex justify-between items-center">
            <div class="flex space-x-6">
                <a href="tel:+97714791891" class="flex items-center hover:text-white transition-colors"><i class="fa-solid fa-phone text-primaryLight mr-2 text-xs"></i> +977-1-4791891</a>
                <a href="mailto:Balephi.energy@rmgroup.com.np" class="flex items-center hover:text-white transition-colors"><i class="fa-solid fa-envelope text-primaryLight mr-2 text-xs"></i> Balephi.energy@rmgroup.com.np</a>
                <span class="flex items-center"><i class="fa-solid fa-location-dot text-primaryLight mr-2 text-xs"></i> New Baneshwor, Kathmandu</span>
            </div>
            <div class="flex items-center space-x-4">
                <a href="https://rmgroup.com.np/" target="_blank" class="text-xs border border-primaryLight/50 text-primaryLight hover:bg-primaryLight hover:text-white px-3 py-1 rounded-full transition-all">Part of RM Group</a>
            </div>
        </div>
    </div>

    <!-- Main Navigation -->
    <header class="bg-white sticky top-0 z-50 transition-all duration-300 shadow-sm" id="navbar">
        <div class="container mx-auto px-4 md:px-8 py-3 flex justify-between items-center">
            <!-- Logo -->
            <a href="index.html" class="flex items-center space-x-3 group">
                <img src="images/logo.jpeg" alt="Balephi Energy Logo" class="h-14 w-auto group-hover:scale-105 transition-transform">
                <div>
                    <h1 class="text-xl font-bold text-slate-800 leading-none tracking-tight">Balephi Energy</h1>
                    <p class="text-[10px] text-primary font-bold tracking-[0.2em] uppercase mt-0.5">Pvt. Ltd.</p>
                </div>
            </a>

            <!-- Desktop Menu -->
            <nav class="hidden lg:flex items-center space-x-1 font-medium text-slate-600 text-[15px]">
                <a href="index.html" class="nav-link px-3 py-2 hover:text-primary transition-colors">Home</a>

                <!-- About Us Dropdown -->
                <div class="relative nav-dropdown">
                    <button class="nav-link px-3 py-2 hover:text-primary transition-colors flex items-center">
                        About Us <i class="fa-solid fa-chevron-down text-[10px] ml-1.5 opacity-60"></i>
                    </button>
                    <div class="dropdown-menu">
                        <a href="chairman.html" class="dropdown-item"><i class="fa-solid fa-quote-left"></i> Chairman Message</a>
                        <a href="team.html" class="dropdown-item"><i class="fa-solid fa-users"></i> Board of Directors</a>
                        <a href="about.html" class="dropdown-item"><i class="fa-solid fa-user-tie"></i> Management / Technical Team</a>
                        <a href="#" class="dropdown-item"><i class="fa-solid fa-sitemap"></i> Committee and Sub Committee</a>
                        <a href="#" class="dropdown-item"><i class="fa-solid fa-hand-holding-heart"></i> CSR</a>
                    </div>
                </div>

                <!-- Downloads Dropdown -->
                <div class="relative nav-dropdown">
                    <button class="nav-link px-3 py-2 hover:text-primary transition-colors flex items-center">
                        Downloads <i class="fa-solid fa-chevron-down text-[10px] ml-1.5 opacity-60"></i>
                    </button>
                    <div class="dropdown-menu">
                        <a href="https://rmgroup.com.np/assets/images/Project%20Sailent%20feature.pdf" target="_blank" class="dropdown-item"><i class="fa-solid fa-book-open"></i> Brochure</a>
                        <a href="#" class="dropdown-item"><i class="fa-solid fa-newspaper"></i> News and Notices</a>
                        <a href="#" class="dropdown-item"><i class="fa-solid fa-chart-line"></i> Q. Reports</a>
                        <a href="#" class="dropdown-item"><i class="fa-solid fa-gavel"></i> AGM</a>
                        <a href="#" class="dropdown-item"><i class="fa-solid fa-file-lines"></i> Share Form</a>
                        <a href="#" class="dropdown-item"><i class="fa-solid fa-shield-halved"></i> Company Policies</a>
                    </div>
                </div>

                <a href="gallery.html" class="nav-link px-3 py-2 hover:text-primary transition-colors">Gallery</a>
                <a href="project.html" class="nav-link px-3 py-2 hover:text-primary transition-colors">Project Update</a>

                <!-- RM Group Dropdown -->
                <div class="relative nav-dropdown">
                    <button class="nav-link px-3 py-2 hover:text-primary transition-colors flex items-center">
                        RM Group <i class="fa-solid fa-chevron-down text-[10px] ml-1.5 opacity-60"></i>
                    </button>
                    <div class="dropdown-menu">
                        <a href="rmgroup.html" class="dropdown-item"><i class="fa-solid fa-handshake"></i> Partners</a>
                        <a href="rmgroup.html#subsidiaries" class="dropdown-item"><i class="fa-solid fa-building-columns"></i> Subsidiaries</a>
                    </div>
                </div>

                <a href="contact.html" class="nav-link px-3 py-2 hover:text-primary transition-colors">Contact</a>
            </nav>

            <!-- CTA Button -->
            <div class="hidden lg:block">
                <a href="project.html" class="bg-primary hover:bg-primaryLight text-white px-5 py-2.5 rounded-full font-medium transition-all shadow-md hover:shadow-lg transform hover:-translate-y-0.5 text-sm">
                    <i class="fa-solid fa-bolt mr-1"></i> 40MW Project
                </a>
            </div>

            <!-- Mobile Menu Button -->
            <button class="lg:hidden text-slate-600 hover:text-primary transition-colors focus:outline-none" id="mobile-menu-btn">
                <i class="fa-solid fa-bars text-2xl"></i>
            </button>
        </div>

        <!-- Mobile Menu -->
        <div class="lg:hidden hidden bg-white border-t border-slate-100 absolute w-full shadow-xl" id="mobile-menu">
            <div class="flex flex-col px-5 py-5 space-y-1 max-h-[80vh] overflow-y-auto">
                <a href="index.html" class="text-primary font-semibold py-2.5 border-b border-slate-100">Home</a>

                <!-- Mobile About -->
                <div class="border-b border-slate-100 py-2.5">
                    <button class="w-full text-left text-slate-700 font-semibold flex justify-between items-center mobile-dropdown-btn">
                        About Us <i class="fa-solid fa-chevron-down text-xs transition-transform"></i>
                    </button>
                    <div class="hidden flex-col pl-4 mt-2 space-y-1 mobile-dropdown-content">
                        <a href="chairman.html" class="text-slate-500 hover:text-primary py-1.5 text-sm"><i class="fa-solid fa-quote-left text-xs mr-2 opacity-50"></i>Chairman Message</a>
                        <a href="team.html" class="text-slate-500 hover:text-primary py-1.5 text-sm"><i class="fa-solid fa-users text-xs mr-2 opacity-50"></i>Board of Directors</a>
                        <a href="about.html" class="text-slate-500 hover:text-primary py-1.5 text-sm"><i class="fa-solid fa-user-tie text-xs mr-2 opacity-50"></i>Management / Technical Team</a>
                        <a href="#" class="text-slate-500 hover:text-primary py-1.5 text-sm"><i class="fa-solid fa-sitemap text-xs mr-2 opacity-50"></i>Committee and Sub Committee</a>
                        <a href="#" class="text-slate-500 hover:text-primary py-1.5 text-sm"><i class="fa-solid fa-hand-holding-heart text-xs mr-2 opacity-50"></i>CSR</a>
                    </div>
                </div>

                <!-- Mobile Downloads -->
                <div class="border-b border-slate-100 py-2.5">
                    <button class="w-full text-left text-slate-700 font-semibold flex justify-between items-center mobile-dropdown-btn">
                        Downloads <i class="fa-solid fa-chevron-down text-xs transition-transform"></i>
                    </button>
                    <div class="hidden flex-col pl-4 mt-2 space-y-1 mobile-dropdown-content">
                        <a href="https://rmgroup.com.np/assets/images/Project%20Sailent%20feature.pdf" target="_blank" class="text-slate-500 hover:text-primary py-1.5 text-sm"><i class="fa-solid fa-book-open text-xs mr-2 opacity-50"></i>Brochure</a>
                        <a href="#" class="text-slate-500 hover:text-primary py-1.5 text-sm"><i class="fa-solid fa-newspaper text-xs mr-2 opacity-50"></i>News and Notices</a>
                        <a href="#" class="text-slate-500 hover:text-primary py-1.5 text-sm"><i class="fa-solid fa-chart-line text-xs mr-2 opacity-50"></i>Q. Reports</a>
                        <a href="#" class="text-slate-500 hover:text-primary py-1.5 text-sm"><i class="fa-solid fa-gavel text-xs mr-2 opacity-50"></i>AGM</a>
                        <a href="#" class="text-slate-500 hover:text-primary py-1.5 text-sm"><i class="fa-solid fa-file-lines text-xs mr-2 opacity-50"></i>Share Form</a>
                        <a href="#" class="text-slate-500 hover:text-primary py-1.5 text-sm"><i class="fa-solid fa-shield-halved text-xs mr-2 opacity-50"></i>Company Policies</a>
                    </div>
                </div>

                <a href="gallery.html" class="text-slate-700 font-semibold py-2.5 border-b border-slate-100">Gallery</a>
                <a href="project.html" class="text-slate-700 font-semibold py-2.5 border-b border-slate-100">Project Update</a>

                <!-- Mobile RM Group -->
                <div class="border-b border-slate-100 py-2.5">
                    <button class="w-full text-left text-slate-700 font-semibold flex justify-between items-center mobile-dropdown-btn">
                        RM Group <i class="fa-solid fa-chevron-down text-xs transition-transform"></i>
                    </button>
                    <div class="hidden flex-col pl-4 mt-2 space-y-1 mobile-dropdown-content">
                        <a href="rmgroup.html" class="text-slate-500 hover:text-primary py-1.5 text-sm"><i class="fa-solid fa-handshake text-xs mr-2 opacity-50"></i>Partners</a>
                        <a href="rmgroup.html#subsidiaries" class="text-slate-500 hover:text-primary py-1.5 text-sm"><i class="fa-solid fa-building-columns text-xs mr-2 opacity-50"></i>Subsidiaries</a>
                    </div>
                </div>

                <a href="contact.html" class="text-slate-700 font-semibold py-2.5">Contact</a>
            </div>
        </div>
    </header>
"""

FOOTER = """
    <!-- Footer -->
    <footer class="bg-dark pt-20 pb-8 border-t-[6px] border-primary mt-auto">
        <div class="container mx-auto px-4 md:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
                <div class="lg:col-span-1">
                    <div class="flex items-center space-x-2 mb-6">
                        <img src="images/logo.jpeg" alt="Balephi Energy Logo" class="h-12 w-auto bg-white rounded p-1">
                        <h3 class="text-2xl font-bold text-white tracking-tight">Balephi Energy</h3>
                    </div>
                    <p class="text-slate-400 mb-6 leading-relaxed">Powering Nepal through clean, sustainable hydropower — a proud entity of the RM Group.</p>
                    <div class="flex space-x-3">
                        <a href="#" class="w-10 h-10 rounded-lg bg-slate-800 text-slate-300 flex items-center justify-center hover:bg-primary hover:text-white transition-all"><i class="fa-brands fa-facebook-f"></i></a>
                        <a href="https://rmgroup.com.np/" target="_blank" class="w-10 h-10 rounded-lg bg-slate-800 text-slate-300 flex items-center justify-center hover:bg-primary hover:text-white transition-all"><i class="fa-solid fa-globe"></i></a>
                    </div>
                </div>
                <div>
                    <h4 class="text-white text-lg font-bold mb-6 relative inline-block pb-2">Quick Links<span class="absolute bottom-0 left-0 w-1/2 h-1 bg-primary"></span></h4>
                    <ul class="space-y-3">
                        <li><a href="index.html" class="text-slate-400 hover:text-primaryLight transition-colors flex items-center"><i class="fa-solid fa-angle-right text-xs mr-2"></i> Home</a></li>
                        <li><a href="about.html" class="text-slate-400 hover:text-primaryLight transition-colors flex items-center"><i class="fa-solid fa-angle-right text-xs mr-2"></i> About BEPL</a></li>
                        <li><a href="project.html" class="text-slate-400 hover:text-primaryLight transition-colors flex items-center"><i class="fa-solid fa-angle-right text-xs mr-2"></i> Balephi Khola HEP</a></li>
                        <li><a href="rmgroup.html" class="text-slate-400 hover:text-primaryLight transition-colors flex items-center"><i class="fa-solid fa-angle-right text-xs mr-2"></i> RM Group</a></li>
                        <li><a href="team.html" class="text-slate-400 hover:text-primaryLight transition-colors flex items-center"><i class="fa-solid fa-angle-right text-xs mr-2"></i> Board of Directors</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-white text-lg font-bold mb-6 relative inline-block pb-2">Project Status<span class="absolute bottom-0 left-0 w-1/2 h-1 bg-primary"></span></h4>
                    <ul class="space-y-3 text-sm text-slate-400">
                        <li><i class="fa-solid fa-check-circle text-secondary mr-2"></i> Feasibility Completed</li>
                        <li><i class="fa-solid fa-check-circle text-secondary mr-2"></i> PPA Signed (2080/05/01)</li>
                        <li><i class="fa-solid fa-check-circle text-secondary mr-2"></i> Generation License (2081/5/7)</li>
                        <li><i class="fa-solid fa-check-circle text-secondary mr-2"></i> Topographical Survey Signed</li>
                        <li><i class="fa-solid fa-spinner text-primaryLight mr-2"></i> Civil work contract ongoing</li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-white text-lg font-bold mb-6 relative inline-block pb-2">Reach Us<span class="absolute bottom-0 left-0 w-1/2 h-1 bg-primary"></span></h4>
                    <ul class="space-y-4">
                        <li class="flex items-start text-slate-400 text-sm"><i class="fa-solid fa-building mt-1 mr-3 text-primaryLight"></i><span><strong>Head Office:</strong><br>New Baneshwor, Kathmandu-10</span></li>
                        <li class="flex items-start text-slate-400 text-sm"><i class="fa-solid fa-map-location-dot mt-1 mr-3 text-primaryLight"></i><span><strong>Site Office:</strong><br>Jugal Rural Municipality, Sindhupalchowk</span></li>
                        <li class="flex items-center text-slate-400 text-sm"><i class="fa-solid fa-phone mr-3 text-primaryLight"></i><span>+977-1-4791891</span></li>
                        <li class="flex items-center text-slate-400 text-sm"><i class="fa-solid fa-envelope mr-3 text-primaryLight"></i><a href="mailto:Balephi.energy@rmgroup.com.np" class="hover:text-white transition-colors">Balephi.energy@rmgroup.com.np</a></li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-slate-800 pt-8 flex flex-col md:flex-row justify-between items-center">
                <p class="text-slate-500 text-sm">&copy; 2025 Balephi Energy Pvt. Ltd. All rights reserved.</p>
                <a href="https://rmgroup.com.np/" target="_blank" class="text-slate-500 hover:text-white text-sm transition-colors mt-2 md:mt-0">RM Group Website</a>
            </div>
        </div>
    </footer>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({ once: true, offset: 50, duration: 800 });
        window.addEventListener('scroll', function() {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 50) { navbar.classList.add('shadow-md'); navbar.querySelector('.container').classList.add('py-2'); navbar.querySelector('.container').classList.remove('py-3'); }
            else { navbar.classList.remove('shadow-md'); navbar.querySelector('.container').classList.add('py-3'); navbar.querySelector('.container').classList.remove('py-2'); }
        });
        document.getElementById('mobile-menu-btn').addEventListener('click', function() {
            document.getElementById('mobile-menu').classList.toggle('hidden');
        });
        document.querySelectorAll('.mobile-dropdown-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const content = this.nextElementSibling;
                const icon = this.querySelector('i');
                content.classList.toggle('hidden');
                content.classList.toggle('flex');
                icon.classList.toggle('rotate-180');
            });
        });
    </script>
</body>
</html>
"""

def write_page(filename, title, body):
    path = f'/Users/sajankafle/Desktop/Balephi/{filename}'
    with open(path, 'w') as f:
        f.write(HEAD.format(title=title))
        f.write(HEADER)
        f.write(body)
        f.write(FOOTER)
    print(f"  ✓ {filename}")

def banner(subtitle, heading, desc):
    return f"""
    <section class="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 py-20 text-white relative overflow-hidden">
        <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-5"></div>
        <div class="absolute top-0 right-0 w-96 h-96 bg-primary/5 rounded-full blur-3xl -mr-48 -mt-48"></div>
        <div class="container mx-auto px-4 md:px-8 relative z-10 text-center">
            <div class="flex items-center justify-center space-x-3 mb-4">
                <span class="h-px w-8 bg-primaryLight"></span>
                <h3 class="text-primaryLight font-bold uppercase tracking-widest text-sm">{subtitle}</h3>
                <span class="h-px w-8 bg-primaryLight"></span>
            </div>
            <h2 class="text-3xl md:text-5xl font-bold">{heading}</h2>
            <p class="text-slate-400 mt-4 max-w-2xl mx-auto">{desc}</p>
        </div>
    </section>
"""

# ═══════════════════════════════════════════════════════════════
# 1. INDEX.HTML — Home Page
# ═══════════════════════════════════════════════════════════════
INDEX_BODY = """
    <!-- Hero Section -->
    <section class="relative h-[85vh] min-h-[600px] flex items-center">
        <div class="absolute inset-0 w-full h-full">
            <img src="images/Picture1.png" alt="Balephi Project Site" class="w-full h-full object-cover">
            <div class="absolute inset-0 hero-overlay"></div>
        </div>
        <div class="container mx-auto px-4 md:px-8 relative z-10">
            <div class="max-w-3xl" data-aos="fade-up" data-aos-duration="1000">
                <div class="inline-block bg-primary/20 border border-primaryLight/30 backdrop-blur-sm text-primaryLight font-semibold px-4 py-1.5 rounded-full text-sm mb-6 uppercase tracking-wider flex items-center w-max">
                    <i class="fa-solid fa-bolt mr-2"></i> 40.00 MW Capacity
                </div>
                <h2 class="text-5xl md:text-6xl lg:text-7xl font-bold text-white mb-6 leading-[1.1]">
                    Balephi Khola <span class="text-transparent bg-clip-text bg-gradient-to-r from-primaryLight to-emerald-400">Hydroelectric</span> Project
                </h2>
                <p class="text-lg md:text-xl text-slate-300 mb-10 max-w-2xl leading-relaxed">
                    Developing affordable, renewable energy projects that enhance productivity and improve Nepalese living standards. Situated in Jugal Rural Municipality, Sindhupalchowk.
                </p>
                <div class="flex flex-wrap gap-4">
                    <a href="project.html" class="bg-primary hover:bg-primaryLight text-white font-medium py-3.5 px-8 rounded-full transition-all shadow-[0_0_20px_rgba(220,38,38,0.3)] hover:shadow-[0_0_25px_rgba(239,68,68,0.5)]">
                        Project Details
                    </a>
                    <a href="about.html" class="bg-white/10 hover:bg-white/20 backdrop-blur-md border border-white/20 text-white font-medium py-3.5 px-8 rounded-full transition-all">
                        Company Profile <i class="fa-solid fa-arrow-right ml-2 text-sm"></i>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Stats Section -->
    <section class="relative -mt-16 z-20 container mx-auto px-4 md:px-8">
        <div class="bg-white rounded-2xl shadow-soft p-8 md:p-10 border border-slate-100" data-aos="fade-up" data-aos-delay="200">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center divide-x divide-slate-100">
                <div class="p-2">
                    <div class="text-4xl font-bold text-primary mb-2">40<span class="text-2xl text-primaryLight">MW</span></div>
                    <div class="text-slate-500 font-medium text-sm uppercase tracking-wider">Installed Capacity</div>
                </div>
                <div class="p-2">
                    <div class="text-4xl font-bold text-primary mb-2">227.6<span class="text-2xl text-primaryLight">GWh</span></div>
                    <div class="text-slate-500 font-medium text-sm uppercase tracking-wider">Total Yearly Energy</div>
                </div>
                <div class="p-2">
                    <div class="text-4xl font-bold text-primary mb-2">284.3<span class="text-2xl text-primaryLight">m</span></div>
                    <div class="text-slate-500 font-medium text-sm uppercase tracking-wider">Gross Head</div>
                </div>
                <div class="p-2">
                    <div class="text-4xl font-bold text-primary mb-2">2029</div>
                    <div class="text-slate-500 font-medium text-sm uppercase tracking-wider">Expected RCOD</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Welcome Section -->
    <section class="py-24 bg-white text-center">
        <div class="container mx-auto px-4 md:px-8">
            <div class="max-w-4xl mx-auto" data-aos="fade-up">
                <div class="flex items-center justify-center space-x-3 mb-4">
                    <span class="h-px w-8 bg-secondary"></span>
                    <h3 class="text-secondary font-bold uppercase tracking-widest text-sm">Welcome to Balephi Energy</h3>
                    <span class="h-px w-8 bg-secondary"></span>
                </div>
                <h2 class="text-3xl md:text-5xl font-bold text-slate-800 mb-6">Committed to Energizing Nepal's Future</h2>
                <p class="text-lg text-slate-600 mb-10 leading-relaxed">Balephi Energy Pvt. Ltd. harnesses the flow of the Himalayas to deliver clean hydropower — building a brighter, greener future for every household in Nepal.</p>
                <div class="flex flex-wrap justify-center gap-4">
                    <a href="about.html" class="inline-flex items-center bg-primary text-white font-semibold hover:bg-primaryLight py-3.5 px-10 rounded-full transition-colors shadow-[0_0_20px_rgba(220,38,38,0.3)]">
                        Learn More About Us <i class="fa-solid fa-arrow-right ml-2 text-sm"></i>
                    </a>
                    <a href="project.html" class="inline-flex items-center bg-secondary text-white font-semibold hover:bg-blue-800 py-3.5 px-10 rounded-full transition-colors shadow-md">
                        View Project Details <i class="fa-solid fa-bolt ml-2 text-sm"></i>
                    </a>
                </div>
            </div>
        </div>
    </section>
"""
write_page('index.html', 'Home', INDEX_BODY)

# ═══════════════════════════════════════════════════════════════
# 2. ABOUT.HTML — Company Profile
# ═══════════════════════════════════════════════════════════════
ABOUT_BODY = banner("About Us", "Background of the Company", "Learn about Balephi Energy Pvt. Ltd. and our mission to develop sustainable hydropower in Nepal.") + """
    <section id="about" class="py-20 overflow-hidden">
        <div class="container mx-auto px-4 md:px-8">
            <div class="flex flex-col lg:flex-row items-center gap-16">
                <div class="w-full lg:w-1/2" data-aos="fade-right">
                    <div class="flex items-center space-x-3 mb-4">
                        <span class="h-px w-12 bg-primary"></span>
                        <h3 class="text-primary font-bold uppercase tracking-widest text-sm">About BEPL</h3>
                    </div>
                    <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold text-slate-800 mb-6 leading-tight">
                        Driving <span class="text-primary">Sustainable</span> Development in Nepal
                    </h2>
                    <div class="text-slate-600 space-y-5 leading-relaxed text-lg mb-8">
                        <p><strong>Balephi Energy Pvt. Ltd. (BEPL)</strong> is the developer of the Balephi Khola Hydroelectric Project. We are focused on developing and implementing affordable renewable energy projects that enhance productivity and improve Nepalese living standards.</p>
                        <p>We are driven to use state-of-the-art technology that maximizes the potential of hydro products in Nepal. BEPL is proudly affiliated with the RM Group, led by Mr. Krishna Prasad Acharya, a conglomerate involved in diverse business sectors across the country.</p>
                    </div>
                    <div class="bg-lightBg p-6 rounded-xl border border-slate-100 shadow-sm mb-8">
                        <h4 class="font-bold text-slate-800 mb-3"><i class="fa-solid fa-flag-checkered text-secondary mr-2"></i> Important Milestones</h4>
                        <ul class="space-y-2 text-slate-600 text-sm">
                            <li><strong>Survey License:</strong> 2076/8/10</li>
                            <li><strong>EIA Approved:</strong> 2079.01.13</li>
                            <li><strong>PPA Signed with NEA:</strong> 2080/05/01</li>
                            <li><strong>Generation License:</strong> 2081/5/7</li>
                        </ul>
                    </div>
                </div>
                <div class="w-full lg:w-1/2 relative" data-aos="fade-left">
                    <div class="grid grid-cols-2 gap-4">
                        <div class="space-y-4">
                            <img src="images/Screenshot%202026-06-11%20at%2020.50.11.png" alt="Balephi Project Site 1" class="w-full h-48 object-cover rounded-2xl shadow-lg hover:scale-105 transition-transform duration-500">
                            <img src="images/Screenshot%202026-06-11%20at%2020.51.07.png" alt="Balephi Project Site 2" class="w-full h-64 object-cover rounded-2xl shadow-lg hover:scale-105 transition-transform duration-500">
                        </div>
                        <div class="space-y-4 pt-8">
                            <img src="images/Screenshot%202026-06-11%20at%2020.51.29.png" alt="Balephi Project Site 3" class="w-full h-64 object-cover rounded-2xl shadow-lg hover:scale-105 transition-transform duration-500">
                            <img src="images/Screenshot%202026-06-11%20at%2020.51.47.png" alt="Balephi Project Site 4" class="w-full h-48 object-cover rounded-2xl shadow-lg hover:scale-105 transition-transform duration-500">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
write_page('about.html', 'About Us', ABOUT_BODY)

# ═══════════════════════════════════════════════════════════════
# 3. CHAIRMAN.HTML — Message from Chairman
# ═══════════════════════════════════════════════════════════════
CHAIRMAN_BODY = banner("Leadership", "Message from the Chairman", "A message from Mr. Krishna Acharya, RM Group Chairman & Chief of Management.") + """
    <section class="py-20 bg-white">
        <div class="container mx-auto px-4 md:px-8">
            <div class="flex flex-col md:flex-row gap-12 items-center max-w-6xl mx-auto">
                <div class="w-full md:w-1/3" data-aos="fade-right">
                    <div class="relative rounded-2xl overflow-hidden shadow-2xl border-8 border-white bg-white">
                        <img src="https://rmgroup.com.np/images/krishnasir.jpg" alt="Mr. Krishna Acharya" class="w-full h-auto object-cover object-top" style="max-height: 450px;">
                    </div>
                </div>
                <div class="w-full md:w-2/3" data-aos="fade-left">
                    <div class="flex items-center space-x-3 mb-4">
                        <span class="h-px w-12 bg-secondary"></span>
                        <h3 class="text-secondary font-bold uppercase tracking-widest text-sm">Message from the Chairman</h3>
                    </div>
                    <h2 class="text-3xl md:text-4xl font-bold text-slate-800 mb-6 leading-tight">Committed to Energizing Nepal's Future</h2>
                    <div class="text-slate-600 space-y-5 leading-relaxed text-lg mb-8 italic border-l-4 border-primary pl-6 bg-slate-50 py-6 pr-6 rounded-r-xl shadow-sm">
                        <p>"As the Chairman of the RM Group and Chief of Management for Balephi Energy, I am proud to oversee our journey toward making Nepal self-reliant in energy production. Our commitment extends beyond generating power; we aim to uplift communities, protect the environment, and foster economic growth across the nation through sustainable hydropower development."</p>
                    </div>
                    <div>
                        <h4 class="text-2xl font-bold text-slate-800">Mr. Krishna Acharya</h4>
                        <p class="text-primary font-medium mt-1">RM Group Chairman / Chief of Management</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
write_page('chairman.html', 'Chairman Message', CHAIRMAN_BODY)

# ═══════════════════════════════════════════════════════════════
# 4. TEAM.HTML — Board of Directors
# ═══════════════════════════════════════════════════════════════
TEAM_BODY = banner("Our Team", "Board of Directors & Management", "Our leadership team driving Nepal's hydropower future.") + """
    <section id="team" class="py-20 bg-slate-50">
        <div class="container mx-auto px-4 md:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-16">
                <div class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-lg transition-all border border-slate-100 text-center p-6" data-aos="fade-up" data-aos-delay="100">
                    <img src="https://rmgroup.com.np/images/krishnasir.jpg" alt="Mr. Krishna Acharya" class="w-24 h-24 mx-auto rounded-full object-cover object-top mb-4 shadow-md border-4 border-primary">
                    <h4 class="text-lg font-bold text-slate-800">Mr. Krishna Acharya</h4>
                    <p class="text-primary font-medium text-sm mb-4">RM Group Chairman / Chief of Management</p>
                    <p class="text-xs text-slate-500 line-clamp-4">Prominent business leader since 1972 (RARA Instant Noodles), involved in hydropower, banking, insurance, tourism. Exec. Chair of Peoples Energy, Chair of Multi Energy.</p>
                </div>
                <div class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-lg transition-all border border-slate-100 text-center p-6" data-aos="fade-up" data-aos-delay="200">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png" alt="Mr. Dil Sundar Shrestha" class="w-24 h-24 mx-auto rounded-full object-cover mb-4 shadow-md border-4 border-slate-200">
                    <h4 class="text-lg font-bold text-slate-800">Mr. Dil Sundar Shrestha</h4>
                    <p class="text-primary font-medium text-sm mb-4">BEPL Chairperson / Project Director</p>
                    <p class="text-xs text-slate-500 line-clamp-4">Established businessman (38 yrs). Exec. Committee Member FNCCI. Director at Peoples Energy, RM Power. Former Director Bindhyabasini Hydro.</p>
                </div>
                <div class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-lg transition-all border border-slate-100 text-center p-6" data-aos="fade-up" data-aos-delay="300">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png" alt="Mr. Sudeep Acharya" class="w-24 h-24 mx-auto rounded-full object-cover mb-4 shadow-md border-4 border-slate-200">
                    <h4 class="text-lg font-bold text-slate-800">Mr. Sudeep Acharya</h4>
                    <p class="text-primary font-medium text-sm mb-4">BEPL Director / Managing Director</p>
                    <p class="text-xs text-slate-500 line-clamp-4">Active in promotion of Hydro-Electricity. Director at Bindhyabasini Hydro, Multi Energy, RM Power. Chairperson of RM Investment.</p>
                </div>
                <div class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-lg transition-all border border-slate-100 text-center p-6" data-aos="fade-up" data-aos-delay="400">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png" alt="Mr. Ashish Shrestha" class="w-24 h-24 mx-auto rounded-full object-cover mb-4 shadow-md border-4 border-slate-200">
                    <h4 class="text-lg font-bold text-slate-800">Mr. Ashish Shrestha</h4>
                    <p class="text-primary font-medium text-sm mb-4">BEPL Director</p>
                    <p class="text-xs text-slate-500 line-clamp-4">Representing Seed Energy Ltd. Over 15 years experience in hotel, consulting, investment, and hydropower sectors.</p>
                </div>
            </div>

            <div class="bg-slate-900 rounded-2xl p-8 md:p-12 text-white" data-aos="fade-up">
                <h3 class="text-2xl font-bold mb-8 text-center">Core Management Team</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="border-l-4 border-primaryLight pl-6">
                        <h4 class="text-xl font-bold text-primaryLight mb-1">Mr. Janardan Aryal</h4>
                        <p class="text-white/80 font-medium mb-3">General Manager / Company Secretary</p>
                        <p class="text-sm text-slate-400">Bachelors in Business Studies. Serving since 2065 in various projects including Khimti II, Rudi Khola, Langtang Khola, and Gupche HEP.</p>
                    </div>
                    <div class="border-l-4 border-secondary pl-6">
                        <h4 class="text-xl font-bold text-secondary mb-1">Mr. Ram Hari Sharma</h4>
                        <p class="text-white/80 font-medium mb-3">Project Manager</p>
                        <p class="text-sm text-slate-400">Master of Advance Studies (MAS) in Tunnel Engineering, M.Sc. Engineering Geology. Involved in numerous mega projects like Upper Karnali (900MW), Tamor-Mewa, Middle Marsyangdi.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
write_page('team.html', 'Board of Directors', TEAM_BODY)

# ═══════════════════════════════════════════════════════════════
# 5. PROJECT.HTML — Balephi Khola HEP
# ═══════════════════════════════════════════════════════════════
PROJECT_BODY = banner("Our Flagship Project", "Balephi Khola HEP", "A 40.00 MW Run-of-River project in Sindhupalchowk District.") + """
    <section id="project" class="py-20 bg-slate-900 text-white relative">
        <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-10"></div>
        <div class="container mx-auto px-4 md:px-8 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
                <div class="bg-slate-800 rounded-2xl p-8 border border-slate-700" data-aos="fade-right">
                    <h3 class="text-2xl font-bold mb-6 text-primaryLight"><i class="fa-solid fa-cogs mr-2"></i> Technical Features</h3>
                    <ul class="divide-y divide-slate-700">
                        <li class="py-4 flex justify-between"><span class="text-slate-400">Type of Project</span><span class="font-semibold text-white">Run of River (ROR)</span></li>
                        <li class="py-4 flex justify-between"><span class="text-slate-400">Design discharge</span><span class="font-semibold text-white">17.1 m³/s</span></li>
                        <li class="py-4 flex justify-between"><span class="text-slate-400">Gross head</span><span class="font-semibold text-white">284.3 m</span></li>
                        <li class="py-4 flex justify-between"><span class="text-slate-400">Installed capacity</span><span class="font-semibold text-white">40.03 MW</span></li>
                        <li class="py-4 flex justify-between"><span class="text-slate-400">Dry period energy</span><span class="font-semibold text-white">35.04 GWh (15.39%)</span></li>
                        <li class="py-4 flex justify-between"><span class="text-slate-400">Wet period energy</span><span class="font-semibold text-white">192.61 GWh (84.61%)</span></li>
                    </ul>
                </div>
                <div class="space-y-8" data-aos="fade-left">
                    <div class="bg-slate-800 rounded-2xl p-8 border border-slate-700">
                        <h3 class="text-xl font-bold mb-4 text-primaryLight"><i class="fa-solid fa-tasks mr-2"></i> Project Status</h3>
                        <p class="text-slate-300 mb-4 leading-relaxed">Currently under construction. Feasibility study, grid connection agreement, PPA with NEA, Generation License, and updated EIA report are all <strong>completed</strong>.</p>
                        <p class="text-slate-300 leading-relaxed">Contracts for topographical survey, design consultant, and explosives have been signed. Private land purchase and civil work contracts are <strong>in progress</strong>.</p>
                    </div>
                    <div class="bg-slate-800 rounded-2xl p-8 border border-slate-700">
                        <h3 class="text-xl font-bold mb-4 text-primaryLight"><i class="fa-solid fa-map-location-dot mr-2"></i> Site Access</h3>
                        <p class="text-slate-300 leading-relaxed"><strong>Route (Approx. 110 km):</strong><br>Kathmandu → Dhulikhel → Dolalghat → Khadichour → Balefi Bazar → Powerhouse</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Salient Features PDF -->
    <section class="py-16 bg-white border-b border-slate-100">
        <div class="container mx-auto px-4 md:px-8">
            <div class="text-center max-w-3xl mx-auto mb-10" data-aos="fade-up">
                <div class="flex items-center justify-center space-x-3 mb-4">
                    <span class="h-px w-8 bg-secondary"></span>
                    <h3 class="text-secondary font-bold uppercase tracking-widest text-sm">Project Specifications</h3>
                    <span class="h-px w-8 bg-secondary"></span>
                </div>
                <h2 class="text-3xl md:text-4xl font-bold text-slate-800 mb-6">Salient Features</h2>
                <p class="text-slate-600 text-lg">Detailed technical specifications and features of the Balephi Khola Hydroelectric Project.</p>
            </div>
            <div class="w-full max-w-5xl mx-auto bg-slate-100 rounded-2xl shadow-inner p-2 md:p-4 border border-slate-200" data-aos="fade-up" data-aos-delay="100">
                <object data="https://rmgroup.com.np/assets/images/Project%20Sailent%20feature.pdf" type="application/pdf" width="100%" height="800px" class="rounded-xl border border-slate-300 shadow-sm bg-white">
                    <embed src="https://rmgroup.com.np/assets/images/Project%20Sailent%20feature.pdf" type="application/pdf" />
                </object>
                <div class="text-center mt-6">
                    <a href="https://rmgroup.com.np/assets/images/Project%20Sailent%20feature.pdf" target="_blank" class="inline-flex items-center bg-primary text-white font-semibold hover:bg-primaryLight py-2.5 px-6 rounded-full transition-colors shadow-md">
                        <i class="fa-solid fa-file-pdf mr-2"></i> View Full Salient Features PDF
                    </a>
                </div>
            </div>
        </div>
    </section>
"""
write_page('project.html', 'Project Details', PROJECT_BODY)

# ═══════════════════════════════════════════════════════════════
# 6. RMGROUP.HTML — RM Group Projects
# ═══════════════════════════════════════════════════════════════
RMGROUP_BODY = banner("Our Group", "RM Group Energy Sector", "A portfolio of hydropower projects across Nepal.") + """
    <section id="rmgroup" class="py-20 bg-slate-50">
        <div class="container mx-auto px-4 md:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16" data-aos="fade-up">
                <h2 class="text-3xl md:text-4xl font-bold text-slate-800 mb-6">RM Group Energy Sector Involvement</h2>
                <p class="text-slate-600 text-lg">Balephi Energy is proud to be part of the RM Group, which boasts an extensive portfolio of hydropower projects across Nepal.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="bg-white p-6 rounded-xl shadow-soft border border-emerald-100 border-t-4 border-t-emerald-500" data-aos="fade-up" data-aos-delay="100">
                    <div class="w-12 h-12 bg-emerald-100 text-emerald-600 rounded-lg flex items-center justify-center text-xl mb-4"><i class="fa-solid fa-money-bill-trend-up"></i></div>
                    <h4 class="text-lg font-bold text-slate-800 mb-4">Revenue Generating</h4>
                    <ul class="space-y-3 text-sm text-slate-600">
                        <li class="flex items-start"><i class="fa-solid fa-check text-emerald-500 mt-1 mr-2"></i> Bindhyabasini Hydropower (Rudi A & B) - 15.4MW</li>
                        <li class="flex items-start"><i class="fa-solid fa-check text-emerald-500 mt-1 mr-2"></i> United Modi Hydropower (Lower Modi 1) - 10MW</li>
                    </ul>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-soft border border-amber-100 border-t-4 border-t-amber-500" data-aos="fade-up" data-aos-delay="200">
                    <div class="w-12 h-12 bg-amber-100 text-amber-600 rounded-lg flex items-center justify-center text-xl mb-4"><i class="fa-solid fa-person-digging"></i></div>
                    <h4 class="text-lg font-bold text-slate-800 mb-4">Under Construction</h4>
                    <ul class="space-y-3 text-sm text-slate-600">
                        <li class="flex items-start"><i class="fa-solid fa-spinner text-amber-500 mt-1 mr-2"></i> Khimti 2 HEP - 48.8MW</li>
                        <li class="flex items-start"><i class="fa-solid fa-spinner text-amber-500 mt-1 mr-2"></i> Langtang Khola HEP - 30MW</li>
                        <li class="flex items-start font-semibold text-primary"><i class="fa-solid fa-bolt text-primary mt-1 mr-2"></i> Balephi Khola HEP - 40MW</li>
                    </ul>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-soft border border-blue-100 border-t-4 border-t-blue-500" data-aos="fade-up" data-aos-delay="300">
                    <div class="w-12 h-12 bg-blue-100 text-blue-600 rounded-lg flex items-center justify-center text-xl mb-4"><i class="fa-solid fa-magnifying-glass-chart"></i></div>
                    <h4 class="text-lg font-bold text-slate-800 mb-4">Under Study</h4>
                    <ul class="space-y-3 text-sm text-slate-600">
                        <li class="flex items-start"><i class="fa-regular fa-file-lines text-blue-500 mt-1 mr-2"></i> Gupche Khola HEP - 7.5MW (Survey done, EIA ongoing)</li>
                        <li class="flex items-start"><i class="fa-regular fa-file-lines text-blue-500 mt-1 mr-2"></i> Ghunsa Khola HEP - 155MW (Survey & EIA ongoing)</li>
                    </ul>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-soft border border-purple-100 border-t-4 border-t-purple-500" data-aos="fade-up" data-aos-delay="400">
                    <div class="w-12 h-12 bg-purple-100 text-purple-600 rounded-lg flex items-center justify-center text-xl mb-4"><i class="fa-solid fa-rocket"></i></div>
                    <h4 class="text-lg font-bold text-slate-800 mb-4">Upcoming Projects</h4>
                    <ul class="space-y-3 text-sm text-slate-600">
                        <li class="flex items-start"><i class="fa-solid fa-arrow-trend-up text-purple-500 mt-1 mr-2"></i> Bheri 8 HEP - 140MW (Processing survey license)</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
"""
write_page('rmgroup.html', 'RM Group', RMGROUP_BODY)

# ═══════════════════════════════════════════════════════════════
# 7. CONTACT.HTML — Contact Us
# ═══════════════════════════════════════════════════════════════
CONTACT_BODY = banner("Get in Touch", "Contact Us", "Have a question about the Balephi Khola Hydroelectric Project? Reach out to us.") + """
    <section class="py-20 bg-slate-50">
        <div class="container mx-auto px-4 md:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-5xl mx-auto">
                <div class="bg-white p-8 rounded-2xl shadow-soft border border-slate-100 relative overflow-hidden group" data-aos="fade-right">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-primary/5 rounded-bl-full -mr-4 -mt-4 transition-transform group-hover:scale-110"></div>
                    <div class="w-16 h-16 bg-primary/10 text-primary rounded-2xl flex items-center justify-center text-2xl mb-6"><i class="fa-solid fa-building"></i></div>
                    <h3 class="text-2xl font-bold text-slate-800 mb-4">Head Office</h3>
                    <ul class="space-y-4 text-slate-600">
                        <li class="flex items-start"><i class="fa-solid fa-location-dot mt-1 mr-3 text-secondary"></i><span>Kathmandu-10, New Baneshwor, Kathmandu, Nepal</span></li>
                        <li class="flex items-center"><i class="fa-solid fa-phone mr-3 text-secondary"></i><span>+977-1-4791891</span></li>
                        <li class="flex items-center"><i class="fa-solid fa-envelope mr-3 text-secondary"></i><a href="mailto:Balephi.energy@rmgroup.com.np" class="hover:text-primary transition-colors">Balephi.energy@rmgroup.com.np</a></li>
                        <li class="flex items-center"><i class="fa-solid fa-globe mr-3 text-secondary"></i><a href="https://rmgroup.com.np/" target="_blank" class="hover:text-primary transition-colors">https://rmgroup.com.np/</a></li>
                    </ul>
                </div>
                <div class="bg-white p-8 rounded-2xl shadow-soft border border-slate-100 relative overflow-hidden group" data-aos="fade-left">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-secondary/5 rounded-bl-full -mr-4 -mt-4 transition-transform group-hover:scale-110"></div>
                    <div class="w-16 h-16 bg-secondary/10 text-secondary rounded-2xl flex items-center justify-center text-2xl mb-6"><i class="fa-solid fa-map-location-dot"></i></div>
                    <h3 class="text-2xl font-bold text-slate-800 mb-4">Site Office</h3>
                    <ul class="space-y-4 text-slate-600">
                        <li class="flex items-start"><i class="fa-solid fa-location-dot mt-1 mr-3 text-primary"></i><span>Jugal Rural Municipality, Sindhupalchowk District, Nepal</span></li>
                    </ul>
                </div>
            </div>
            <div class="max-w-5xl mx-auto mt-12" data-aos="fade-up">
                <div class="bg-white rounded-2xl shadow-soft border border-slate-100 p-2 overflow-hidden">
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d220849.99874786!2d85.6!3d27.85!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39eb6915a2a8b5ab%3A0x5bb4c3f37e0f34a0!2sSindhupalchowk!5e0!3m2!1sen!2snp!4v1718105000000!5m2!1sen!2snp" width="100%" height="400" style="border:0; border-radius: 1rem;" allowfullscreen="" loading="lazy"></iframe>
                </div>
            </div>
        </div>
    </section>
"""
write_page('contact.html', 'Contact Us', CONTACT_BODY)

print("\\n✅ All 7 pages built successfully with dropdown menus!")
