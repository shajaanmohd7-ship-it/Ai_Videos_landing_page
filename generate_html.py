import json

with open('portfolio_data.json', 'r', encoding='utf-8') as f:
    videos = json.load(f)

videos_json_str = json.dumps(videos, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth overflow-x-hidden">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
    <title>Sociallyconnect | Video Production Portfolio</title>
    <meta name="description" content="Showcase of 50+ commercial video productions, corporate TVCs, educational films, and narrative shorts by Sociallyconnect.">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                screens: {{
                    'xs': '420px',
                    'sm': '640px',
                    'md': '768px',
                    'lg': '1024px',
                    'xl': '1280px',
                    '2xl': '1536px',
                }},
                extend: {{
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                        display: ['"Space Grotesk"', 'sans-serif'],
                    }},
                    colors: {{
                        brand: {{
                            50: '#eef2ff',
                            100: '#e0e7ff',
                            400: '#818cf8',
                            500: '#6366f1',
                            600: '#4f46e5',
                            glow: '#06b6d4',
                            magenta: '#ec4899',
                        }},
                        dark: {{
                            base: '#07090e',
                            surface: '#0f1420',
                            card: '#141b2d',
                            border: '#1f293d',
                            hover: '#283552',
                        }}
                    }},
                    animation: {{
                        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                    }}
                }}
            }}
        }}
    </script>
    
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    
    <style>
        /* Strict global horizontal overflow prevention */
        *, *::before, *::after {{
            box-sizing: border-box;
        }}
        html {{
            width: 100%;
            max-width: 100%;
            overflow-x: hidden;
            overflow-x: clip;
            -webkit-text-size-adjust: 100%;
        }}
        body {{
            width: 100%;
            max-width: 100%;
            overflow-x: hidden;
            overflow-x: clip;
            position: relative;
        }}

        /* Mobile & desktop scrollbars */
        ::-webkit-scrollbar {{
            width: 5px;
            height: 5px;
        }}
        ::-webkit-scrollbar-track {{
            background: #07090e;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #1f293d;
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #06b6d4;
        }}

        /* Hide horizontal scrollbar while keeping smooth touch scroll */
        .no-scrollbar::-webkit-scrollbar {{
            display: none;
        }}
        .no-scrollbar {{
            -ms-overflow-style: none;
            scrollbar-width: none;
            -webkit-overflow-scrolling: touch;
        }}
        
        /* Glassmorphism */
        .glass-panel {{
            background: rgba(15, 20, 32, 0.92);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }}
        .glass-card {{
            background: rgba(20, 27, 45, 0.6);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.06);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        @media (hover: hover) {{
            .glass-card:hover {{
                border-color: rgba(6, 182, 212, 0.4);
                transform: translateY(-4px);
                box-shadow: 0 16px 32px -8px rgba(6, 182, 212, 0.15), 0 0 0 1px rgba(6, 182, 212, 0.2);
            }}
        }}
        .glass-card:active {{
            transform: scale(0.99);
        }}
        
        .hero-glow {{
            position: absolute;
            width: 480px;
            height: 480px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, rgba(6, 182, 212, 0.08) 50%, transparent 70%);
            filter: blur(60px);
            pointer-events: none;
            z-index: 0;
        }}

        /* Safe area for iPhone home indicator */
        .safe-bottom {{
            padding-bottom: max(0.75rem, env(safe-area-inset-bottom));
        }}
        
        /* Dynamic viewport height for mobile */
        .modal-height {{
            height: 100dvh;
        }}
        @media (min-width: 640px) {{
            .modal-height {{
                height: 90vh;
            }}
        }}

        /* Video Player Container */
        .video-player-container {{
            width: 100%;
            height: 100%;
            background: #000000;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }}
    </style>
</head>
<body class="bg-dark-base text-slate-100 font-sans selection:bg-cyan-500 selection:text-white min-h-screen flex flex-col relative w-full overflow-x-hidden antialiased">

    <!-- Ambient background light effects (Confined strictly in an overflow-hidden wrapper so they never spill horizontally) -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none z-0" aria-hidden="true">
        <div class="hero-glow top-0 left-1/2 -translate-x-1/2"></div>
        <div class="hero-glow top-96 left-0 opacity-30"></div>
        <div class="hero-glow top-[1200px] right-0 opacity-30"></div>
    </div>

    <!-- Navigation Header -->
    <header class="sticky top-0 z-40 glass-panel border-b border-dark-border/80 w-full">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-14 sm:h-18 flex items-center justify-between gap-3">
            
            <!-- Clean Brand Title (No logo icon, no AI badge) -->
            <a href="#" class="font-display font-extrabold text-lg sm:text-2xl text-white tracking-tight hover:text-cyan-400 transition-colors truncate">
                Sociallyconnect
            </a>

            <!-- Desktop Nav items -->
            <nav class="hidden md:flex items-center space-x-8 text-sm font-medium text-slate-300">
                <a href="#featured" class="hover:text-cyan-400 transition-colors">Spotlight</a>
                <a href="#portfolio" class="hover:text-cyan-400 transition-colors">All Videos (50)</a>
            </nav>

            <!-- Header Actions -->
            <div class="flex items-center space-x-2 sm:space-x-3 flex-shrink-0">
                <a href="https://drive.google.com/drive/folders/1BFs6zc9Vvdx-_Lsy_rB221ImoEe_6Gec" target="_blank" rel="noopener noreferrer" 
                   class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-dark-card hover:bg-dark-hover border border-dark-border text-xs font-semibold text-slate-300 hover:text-white transition-all">
                    <i data-lucide="folder-git-2" class="w-3.5 h-3.5 text-cyan-400"></i>
                    <span>Drive Folder</span>
                </a>
                <a href="#portfolio" class="inline-flex items-center gap-1.5 px-3 sm:px-4 py-1.5 sm:py-2 rounded-lg bg-gradient-to-r from-cyan-500 to-brand-600 hover:from-cyan-400 hover:to-brand-500 text-xs font-bold text-white shadow-md shadow-cyan-500/25 active:scale-95 transition-all">
                    <i data-lucide="play" class="w-3 h-3 sm:w-3.5 sm:h-3.5 fill-current"></i>
                    <span>50 Videos</span>
                </a>
            </div>
        </div>
    </header>

    <!-- Main Content Container with strict w-full overflow-hidden -->
    <main class="w-full overflow-x-hidden flex-1 flex flex-col">
        <!-- Hero Section -->
        <section class="relative pt-6 pb-10 sm:pt-14 sm:pb-20 overflow-hidden z-10 w-full">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 sm:gap-12 items-center w-full">
                    
                    <!-- Hero Left: Content -->
                    <div class="lg:col-span-7 space-y-4 sm:space-y-6 text-center lg:text-left w-full">
                        
                        <h1 class="font-display font-extrabold text-2xl xs:text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-[1.2] break-words">
                            Cinematic AI Stories & High-Converting <span class="bg-gradient-to-r from-cyan-400 via-sky-300 to-indigo-400 bg-clip-text text-transparent">Commercial TVCs</span>
                        </h1>

                        <p class="text-xs sm:text-base lg:text-lg text-slate-300 max-w-2xl mx-auto lg:mx-0 leading-relaxed">
                            Explore our comprehensive gallery of 50+ custom-produced videos — ranging from premium D2C brand commercials and financial explainers to global study campaigns and emotional story films.
                        </p>

                        <!-- CTAs -->
                        <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-3 pt-1 w-full">
                            <a href="#portfolio" class="w-full sm:w-auto px-5 py-3 rounded-xl bg-gradient-to-r from-cyan-500 to-indigo-600 hover:from-cyan-400 hover:to-indigo-500 text-white font-semibold text-xs sm:text-sm shadow-xl shadow-cyan-500/20 flex items-center justify-center gap-2 group transition-all">
                                <span>Browse 50 Portfolio Videos</span>
                                <i data-lucide="arrow-down" class="w-4 h-4 group-hover:translate-y-1 transition-transform"></i>
                            </a>
                            <button onclick="openModalById('1juU8pgjoOwNnAc8_H4sNLR64jbjzxnCa')" class="w-full sm:w-auto px-5 py-3 rounded-xl glass-card hover:bg-dark-hover text-slate-200 hover:text-white font-semibold text-xs sm:text-sm flex items-center justify-center gap-2 transition-all">
                                <i data-lucide="play-circle" class="w-4 h-4 text-cyan-400"></i>
                                <span>Watch Spotlight Reel</span>
                            </button>
                        </div>

                        <!-- Metric Counters -->
                        <div class="grid grid-cols-3 gap-2 sm:gap-6 pt-5 sm:pt-8 border-t border-dark-border/60 max-w-lg mx-auto lg:mx-0 text-center sm:text-left w-full">
                            <div class="p-1 sm:p-0">
                                <div class="font-display font-bold text-lg sm:text-3xl text-white">50+</div>
                                <div class="text-[10px] sm:text-xs text-slate-400 font-medium mt-0.5 truncate">Videos Produced</div>
                            </div>
                            <div class="p-1 sm:p-0">
                                <div class="font-display font-bold text-lg sm:text-3xl text-cyan-400">5+</div>
                                <div class="text-[10px] sm:text-xs text-slate-400 font-medium mt-0.5 truncate">Industry Sectors</div>
                            </div>
                            <div class="p-1 sm:p-0">
                                <div class="font-display font-bold text-lg sm:text-3xl text-indigo-400">1080p+</div>
                                <div class="text-[10px] sm:text-xs text-slate-400 font-medium mt-0.5 truncate">Master Quality</div>
                            </div>
                        </div>
                    </div>

                    <!-- Hero Right: Interactive Spotlight Feature -->
                    <div class="lg:col-span-5 w-full" id="featured">
                        <div class="relative rounded-2xl p-[1px] bg-gradient-to-b from-cyan-500/40 via-indigo-500/20 to-transparent shadow-2xl shadow-cyan-500/10 w-full">
                            <div class="bg-dark-surface rounded-2xl overflow-hidden p-3.5 sm:p-5 space-y-3 sm:space-y-4 w-full">
                                <!-- Card Header -->
                                <div class="flex items-center justify-between">
                                    <div class="flex items-center gap-2">
                                        <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
                                        <span class="text-[10px] sm:text-[11px] font-bold uppercase tracking-wider text-slate-300">Spotlight Feature</span>
                                    </div>
                                    <span class="text-[9px] sm:text-[10px] font-semibold px-2 py-0.5 rounded-md bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Finance & TVC</span>
                                </div>

                                <!-- Video Preview Thumbnail Container -->
                                <div class="relative rounded-xl overflow-hidden aspect-video bg-dark-card group cursor-pointer border border-dark-border w-full"
                                     onclick="openModalById('1juU8pgjoOwNnAc8_H4sNLR64jbjzxnCa')">
                                    <img src="thumbnails/1juU8pgjoOwNnAc8_H4sNLR64jbjzxnCa.jpg" 
                                         alt="BKC Finance Short Brand Movie" 
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                                         onerror="this.onerror=null; this.src='https://lh3.googleusercontent.com/d/1juU8pgjoOwNnAc8_H4sNLR64jbjzxnCa=w640'">
                                    
                                    <div class="absolute inset-0 bg-dark-base/40 group-hover:bg-dark-base/20 transition-colors flex items-center justify-center">
                                        <div class="w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-cyan-500/90 text-dark-base flex items-center justify-center shadow-xl shadow-cyan-500/40 group-hover:scale-110 transition-transform">
                                            <i data-lucide="play" class="w-5 h-5 sm:w-6 sm:h-6 fill-current ml-0.5"></i>
                                        </div>
                                    </div>

                                    <div class="absolute bottom-2 right-2 px-2 py-0.5 rounded bg-black/80 backdrop-blur-sm text-[9px] sm:text-[10px] font-bold text-white flex items-center gap-1">
                                        <i data-lucide="sparkles" class="w-3 h-3 text-cyan-400"></i>
                                        <span>Master Cut</span>
                                    </div>
                                </div>

                                <!-- Spotlight Info -->
                                <div>
                                    <h3 class="font-display font-bold text-sm sm:text-base text-white">BKC Finance Short Brand Movie</h3>
                                    <p class="text-xs text-slate-400 mt-1 line-clamp-2">A high-engagement corporate brand film combining hyper-realistic AI visuals and compelling financial storytelling.</p>
                                </div>

                                <button onclick="openModalById('1juU8pgjoOwNnAc8_H4sNLR64jbjzxnCa')" 
                                        class="w-full py-2 sm:py-2.5 rounded-lg bg-cyan-500/10 hover:bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 text-xs font-semibold flex items-center justify-center gap-2 transition-colors">
                                <i data-lucide="play" class="w-3.5 h-3.5 fill-current"></i>
                                <span>Play in Google Drive Player</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Main Portfolio Gallery Section -->
        <section id="portfolio" class="relative py-10 sm:py-16 bg-dark-surface/50 border-t border-dark-border z-10 w-full overflow-hidden">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
                
                <!-- Section Header -->
                <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 sm:gap-6 pb-6 sm:pb-8 w-full">
                    <div>
                        <h2 class="font-display font-extrabold text-xl sm:text-3xl md:text-4xl text-white">
                            Curated Works & Productions
                        </h2>
                        <p class="text-xs sm:text-sm text-slate-400 mt-1 max-w-xl">
                            Filter by category or search by keywords to explore our video campaigns. Tap any video to watch.
                        </p>
                    </div>

                    <!-- Live Search Box -->
                    <div class="w-full md:w-80">
                        <div class="relative w-full">
                            <i data-lucide="search" class="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2"></i>
                            <input type="text" id="searchInput" placeholder="Search videos (e.g. Imerbela, NPS)..." 
                                   class="w-full pl-9 pr-8 py-2.5 bg-dark-card border border-dark-border rounded-xl text-xs sm:text-sm text-white placeholder-slate-400 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 transition-all">
                            <button id="clearSearchBtn" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white" onclick="clearSearch()">
                                <i data-lucide="x" class="w-4 h-4"></i>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Filter Categories Tabs (Zero negative margins, clean horizontal touch scrolling) -->
                <div class="w-full overflow-hidden">
                    <div class="flex items-center gap-2 overflow-x-auto pb-3 pt-1 no-scrollbar border-b border-dark-border/60 w-full">
                        <button onclick="setCategory('All')" data-cat="All" class="filter-btn active-tab px-3.5 py-1.5 sm:px-4 sm:py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-all bg-cyan-500 text-dark-base shadow-md shadow-cyan-500/20 flex-shrink-0">
                            All (50)
                        </button>
                        <button onclick="setCategory('Commercials & Ads')" data-cat="Commercials & Ads" class="filter-btn px-3.5 py-1.5 sm:px-4 sm:py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-all bg-dark-card hover:bg-dark-hover text-slate-300 hover:text-white border border-dark-border flex-shrink-0">
                            Commercials (18)
                        </button>
                        <button onclick="setCategory('Finance & Corporate')" data-cat="Finance & Corporate" class="filter-btn px-3.5 py-1.5 sm:px-4 sm:py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-all bg-dark-card hover:bg-dark-hover text-slate-300 hover:text-white border border-dark-border flex-shrink-0">
                            Finance (12)
                        </button>
                        <button onclick="setCategory('Education & Global')" data-cat="Education & Global" class="filter-btn px-3.5 py-1.5 sm:px-4 sm:py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-all bg-dark-card hover:bg-dark-hover text-slate-300 hover:text-white border border-dark-border flex-shrink-0">
                            Education (11)
                        </button>
                        <button onclick="setCategory('Narrative & Drama')" data-cat="Narrative & Drama" class="filter-btn px-3.5 py-1.5 sm:px-4 sm:py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-all bg-dark-card hover:bg-dark-hover text-slate-300 hover:text-white border border-dark-border flex-shrink-0">
                            Narrative (6)
                        </button>
                        <button onclick="setCategory('AI & Showreels')" data-cat="AI & Showreels" class="filter-btn px-3.5 py-1.5 sm:px-4 sm:py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-all bg-dark-card hover:bg-dark-hover text-slate-300 hover:text-white border border-dark-border flex-shrink-0">
                            AI & Reels (3)
                        </button>
                    </div>
                </div>

                <!-- Results Counter & Sort bar -->
                <div class="flex items-center justify-between text-[11px] sm:text-xs text-slate-400 py-3 w-full">
                    <div id="resultsCount">Showing all 50 videos</div>
                    <div class="flex items-center gap-1.5">
                        <span class="hidden sm:inline">Sort:</span>
                        <select id="sortSelect" onchange="sortVideos()" class="bg-dark-card border border-dark-border rounded-lg px-2 py-1 text-slate-300 text-xs focus:outline-none focus:border-cyan-500">
                            <option value="default">Default</option>
                            <option value="az">Title (A - Z)</option>
                            <option value="category">Category</option>
                        </select>
                    </div>
                </div>

                <!-- Video Grid (Strictly confined, 1 column on phones, 2 on sm, 3 on lg, 4 on xl) -->
                <div id="videoGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 sm:gap-6 pt-2 pb-16 w-full">
                    <!-- Video Cards dynamically rendered -->
                </div>

                <!-- Empty State when search has no results -->
                <div id="emptyState" class="hidden text-center py-16 w-full">
                    <div class="w-14 h-14 mx-auto rounded-full bg-dark-card border border-dark-border flex items-center justify-center text-slate-500 mb-3">
                        <i data-lucide="video-off" class="w-6 h-6"></i>
                    </div>
                    <h3 class="font-display font-bold text-base text-white">No videos found</h3>
                    <p class="text-xs text-slate-400 mt-1 max-w-xs mx-auto">Try searching for a different keyword or switch to another category filter.</p>
                    <button onclick="clearSearch()" class="mt-4 px-4 py-1.5 rounded-lg bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-xs font-semibold hover:bg-cyan-500/20 transition-colors">
                        Reset Filters
                    </button>
                </div>

            </div>
        </section>
    </main>

    <!-- Clean Minimal Footer -->
    <footer class="py-6 sm:py-8 bg-dark-base border-t border-dark-border/60 text-[11px] sm:text-xs text-slate-500 z-10 safe-bottom w-full">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left w-full">
            <p>© 2026 Sociallyconnect. All rights reserved.</p>
            <div class="flex items-center gap-3 justify-center sm:justify-start">
                <a href="https://drive.google.com/drive/folders/1BFs6zc9Vvdx-_Lsy_rB221ImoEe_6Gec" target="_blank" rel="noopener noreferrer" 
                   class="hover:text-cyan-400 flex items-center gap-1.5 transition-colors">
                    <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                    <span>Google Drive Folder (50 Videos)</span>
                </a>
            </div>
        </div>
    </footer>

    <!-- ======================================================== -->
    <!-- 100% RESPONSIVE GOOGLE DRIVE PLAYER MODAL (ALL MOBILES)   -->
    <!-- ======================================================== -->
    <div id="videoModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-0 sm:p-4 md:p-6 bg-dark-base/95 backdrop-blur-xl opacity-0 transition-opacity duration-300">
        
        <!-- Modal Backdrop click to close -->
        <div class="absolute inset-0" onclick="closeModal()"></div>

        <!-- Desktop Floating Left Arrow -->
        <button onclick="prevVideo()" title="Previous Video (Left Arrow)" 
                class="hidden xl:flex absolute left-4 top-1/2 -translate-y-1/2 z-20 w-12 h-12 rounded-full bg-dark-surface/90 hover:bg-cyan-500 hover:text-dark-base border border-dark-border hover:border-cyan-400 text-slate-200 items-center justify-center shadow-2xl transition-all group">
            <i data-lucide="chevron-left" class="w-6 h-6 group-hover:-translate-x-0.5 transition-transform"></i>
        </button>

        <!-- Desktop Floating Right Arrow -->
        <button onclick="nextVideo()" title="Next Video (Right Arrow)" 
                class="hidden xl:flex absolute right-4 top-1/2 -translate-y-1/2 z-20 w-12 h-12 rounded-full bg-dark-surface/90 hover:bg-cyan-500 hover:text-dark-base border border-dark-border hover:border-cyan-400 text-slate-200 items-center justify-center shadow-2xl transition-all group">
            <i data-lucide="chevron-right" class="w-6 h-6 group-hover:translate-x-0.5 transition-transform"></i>
        </button>

        <!-- Modal Dialog Box (Full-screen on mobile, rounded card on tablet/desktop) -->
        <div class="relative w-full sm:max-w-6xl modal-height bg-dark-surface sm:border sm:border-dark-border sm:rounded-2xl shadow-2xl overflow-hidden z-10 flex flex-col scale-95 sm:scale-95 transition-transform duration-300" id="modalBox">
            
            <!-- Modal Header (Compact & Safe on all phone widths) -->
            <div class="px-3.5 sm:px-6 py-2 sm:py-3 border-b border-dark-border bg-dark-card/95 flex items-center justify-between gap-2 flex-shrink-0 w-full">
                
                <!-- Left: Title & Category -->
                <div class="flex items-center gap-2 overflow-hidden min-w-0 pr-1 flex-1">
                    <span id="modalCategory" class="px-2 py-0.5 rounded-full text-[9px] sm:text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 whitespace-nowrap">
                        Category
                    </span>
                    <h3 id="modalTitle" class="font-display font-bold text-xs sm:text-base text-white truncate" title="Video Title">
                        Video Title
                    </h3>
                </div>

                <!-- Right Header Actions -->
                <div class="flex items-center gap-1.5 sm:gap-2 flex-shrink-0">
                    <!-- Counter badge -->
                    <span id="modalCounter" class="text-[10px] sm:text-xs font-mono font-bold text-cyan-400 px-1.5 sm:px-2 py-0.5 rounded bg-dark-base/80 border border-dark-border">
                        1 / 50
                    </span>

                    <!-- Open in Google Drive -->
                    <a id="modalDriveLink" href="#" target="_blank" rel="noopener noreferrer" 
                       title="Open directly in Google Drive"
                       class="p-1.5 sm:p-2 rounded-lg bg-dark-hover hover:bg-slate-700 text-slate-300 hover:text-white border border-dark-border transition-colors">
                        <i data-lucide="external-link" class="w-3.5 h-3.5 sm:w-4 sm:h-4 text-cyan-400"></i>
                    </a>
                    
                    <!-- Close Button -->
                    <button onclick="closeModal()" title="Close (Esc)" 
                            class="p-1.5 sm:p-2 rounded-lg bg-dark-hover hover:bg-red-500/20 text-slate-300 hover:text-red-400 border border-dark-border transition-colors">
                        <i data-lucide="x" class="w-4 h-4 sm:w-5 sm:h-5"></i>
                    </button>
                </div>
            </div>

            <!-- Normal Browser Native Video Player Container -->
            <div class="video-player-container relative w-full flex-1 min-h-0 bg-black overflow-hidden flex items-center justify-center">
                <!-- Loading spinner -->
                <div id="playerLoader" class="absolute inset-0 flex flex-col items-center justify-center text-slate-400 gap-2.5 bg-black/85 z-20 pointer-events-none transition-opacity duration-300">
                    <i data-lucide="loader-2" class="w-8 h-8 sm:w-10 sm:h-10 animate-spin text-cyan-400"></i>
                    <span class="text-xs font-medium text-slate-300">Loading video...</span>
                </div>

                <!-- Error fallback -->
                <div id="playerError" class="hidden absolute inset-0 flex flex-col items-center justify-center text-slate-300 gap-3 bg-dark-base/95 z-25 p-6 text-center">
                    <i data-lucide="alert-circle" class="w-10 h-10 text-amber-400"></i>
                    <p class="text-sm font-medium text-slate-200">Video streaming direct link</p>
                    <a id="errorDriveBtn" href="#" target="_blank" rel="noopener noreferrer" 
                       class="px-4 py-2 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-dark-base font-bold text-xs flex items-center gap-2 transition-all">
                        <i data-lucide="external-link" class="w-4 h-4"></i>
                        <span>Open in Google Drive</span>
                    </a>
                </div>

                <!-- Normal Browser Native Video Player -->
                <video id="browserVideoPlayer" 
                       class="w-full h-full object-contain" 
                       controls 
                       playsinline 
                       webkit-playsinline 
                       preload="metadata"
                       controlslist="nodownload">
                </video>
            </div>

            <!-- Mobile & Desktop Bottom Navigation Bar (Thumb Friendly) -->
            <div class="px-3.5 sm:px-6 py-2.5 sm:py-3 border-t border-dark-border bg-dark-card/95 flex flex-col sm:flex-row items-center justify-between gap-2 flex-shrink-0 safe-bottom w-full">
                
                <div class="flex items-center justify-between w-full sm:w-auto gap-3">
                    <!-- Prev Button -->
                    <button onclick="prevVideo()" class="flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 px-3.5 py-2 sm:px-4 sm:py-2 rounded-xl bg-dark-surface hover:bg-dark-hover border border-dark-border text-xs sm:text-sm font-semibold text-slate-200 hover:text-white active:scale-95 transition-all">
                        <i data-lucide="chevron-left" class="w-4 h-4"></i>
                        <span>Previous</span>
                    </button>

                    <!-- Next Button -->
                    <button onclick="nextVideo()" class="flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 px-3.5 py-2 sm:px-5 sm:py-2 rounded-xl bg-gradient-to-r from-cyan-500 to-indigo-600 hover:from-cyan-400 hover:to-indigo-500 text-xs sm:text-sm font-bold text-white shadow-md shadow-cyan-500/25 active:scale-95 transition-all">
                        <span>Next Video</span>
                        <i data-lucide="chevron-right" class="w-4 h-4"></i>
                    </button>
                </div>

                <!-- Helpful Tip on mobile -->
                <div class="text-[10px] sm:text-xs text-slate-400 font-medium text-center">
                    <span class="sm:hidden text-cyan-400">💡 Standard browser player: 3-dots me speed & settings available hain</span>
                    <span class="hidden sm:inline text-slate-500">Keyboard: Space Play/Pause | ← Prev | → Next | Esc Close</span>
                </div>
            </div>

        </div>
    </div>

    <!-- Embedded Video Catalog Data -->
    <script>
        const ALL_VIDEOS = {videos_json_str};
        
        let currentFiltered = [...ALL_VIDEOS];
        let currentCategory = 'All';
        let searchQuery = '';
        let currentModalIndex = 0;

        // Initialize Page
        document.addEventListener('DOMContentLoaded', () => {{
            renderVideoGrid(ALL_VIDEOS);
            lucide.createIcons();
            
            // Search input listener
            document.getElementById('searchInput').addEventListener('input', (e) => {{
                searchQuery = e.target.value.toLowerCase().trim();
                const clearBtn = document.getElementById('clearSearchBtn');
                if (searchQuery) {{
                    clearBtn.classList.remove('hidden');
                }} else {{
                    clearBtn.classList.add('hidden');
                }}
                applyFilters();
            }});

            // Keyboard navigation for modal
            document.addEventListener('keydown', (e) => {{
                const modal = document.getElementById('videoModal');
                if (!modal.classList.contains('hidden')) {{
                    if (e.key === 'Escape') closeModal();
                    if (e.key === 'ArrowLeft') prevVideo();
                    if (e.key === 'ArrowRight') nextVideo();
                }}
            }});
        }});

        // Render Cards into Grid
        function renderVideoGrid(videos) {{
            const grid = document.getElementById('videoGrid');
            const emptyState = document.getElementById('emptyState');
            const counter = document.getElementById('resultsCount');

            counter.innerText = `Showing ${{videos.length}} of ${{ALL_VIDEOS.length}} videos`;

            if (videos.length === 0) {{
                grid.innerHTML = '';
                emptyState.classList.remove('hidden');
                return;
            }}

            emptyState.classList.add('hidden');
            grid.innerHTML = videos.map((v, idx) => {{
                return `
                <div class="glass-card rounded-xl sm:rounded-2xl overflow-hidden flex flex-col group cursor-pointer active:scale-[0.99] transition-transform w-full" onclick="openModalByIndex(${{idx}})">
                    <!-- Thumbnail Container -->
                    <div class="relative aspect-video bg-dark-card overflow-hidden w-full">
                        <img src="${{v.thumbnail}}" 
                             alt="${{v.title}}" 
                             loading="lazy"
                             referrerpolicy="no-referrer"
                             class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                             onerror="if(this.src !== '${{v.remoteThumbnail}}') {{ this.src = '${{v.remoteThumbnail}}'; }} else {{ this.onerror=null; this.src='https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=640&q=80'; }}" />

                        <!-- Dark Overlay & Play Button -->
                        <div class="absolute inset-0 bg-dark-base/40 group-hover:bg-dark-base/20 transition-all flex items-center justify-center">
                            <div class="w-10 h-10 sm:w-11 sm:h-11 rounded-full bg-cyan-500/90 text-dark-base flex items-center justify-center shadow-lg shadow-cyan-500/30 group-hover:scale-110 transition-transform">
                                <i data-lucide="play" class="w-4 h-4 sm:w-5 sm:h-5 fill-current ml-0.5"></i>
                            </div>
                        </div>

                        <!-- Category Pill (Top-Left) -->
                        <div class="absolute top-2 left-2 sm:top-2.5 sm:left-2.5">
                            <span class="px-2 py-0.5 rounded-md text-[9px] sm:text-[10px] font-bold bg-dark-base/80 backdrop-blur-md text-cyan-300 border border-dark-border">
                                ${{v.category}}
                            </span>
                        </div>

                        <!-- Direct Drive link icon (Top-Right) -->
                        <a href="${{v.driveUrl}}" target="_blank" rel="noopener noreferrer" 
                           onclick="event.stopPropagation()"
                           title="Open in Drive"
                           class="absolute top-2 right-2 sm:top-2.5 sm:right-2.5 w-6 h-6 sm:w-7 sm:h-7 rounded-md bg-dark-base/80 backdrop-blur-md flex items-center justify-center text-slate-300 hover:text-white border border-dark-border transition-colors">
                            <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                        </a>
                    </div>

                    <!-- Card Body -->
                    <div class="p-3 sm:p-4 flex-1 flex flex-col justify-between w-full">
                        <div class="w-full">
                            <h3 class="font-display font-bold text-xs sm:text-sm text-white group-hover:text-cyan-300 transition-colors line-clamp-1" title="${{v.title}}">
                                ${{v.title}}
                            </h3>
                            <p class="text-[11px] sm:text-xs text-slate-400 mt-1 line-clamp-2 leading-relaxed">
                                ${{v.description}}
                            </p>
                        </div>

                        <div class="pt-2.5 mt-2.5 sm:pt-3 sm:mt-3 border-t border-dark-border/50 flex items-center justify-between text-[10px] sm:text-[11px] text-slate-400 w-full gap-2">
                            <span class="font-mono text-slate-500 truncate min-w-0 flex-1">${{v.filename}}</span>
                            <span class="font-semibold text-cyan-400 flex items-center gap-1 group-hover:translate-x-1 transition-transform flex-shrink-0">
                                Watch <i data-lucide="arrow-right" class="w-3 h-3"></i>
                            </span>
                        </div>
                    </div>
                </div>
                `;
            }}).join('');

            lucide.createIcons();
        }}

        // Filter and Search logic
        function setCategory(cat) {{
            currentCategory = cat;
            document.querySelectorAll('.filter-btn').forEach(btn => {{
                if (btn.dataset.cat === cat) {{
                    btn.className = "filter-btn active-tab px-3.5 py-1.5 sm:px-4 sm:py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-all bg-cyan-500 text-dark-base shadow-md shadow-cyan-500/20 flex-shrink-0";
                }} else {{
                    btn.className = "filter-btn px-3.5 py-1.5 sm:px-4 sm:py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-all bg-dark-card hover:bg-dark-hover text-slate-300 hover:text-white border border-dark-border flex-shrink-0";
                }}
            }});
            applyFilters();
        }}

        function applyFilters() {{
            currentFiltered = ALL_VIDEOS.filter(v => {{
                const matchCategory = (currentCategory === 'All') || (v.category === currentCategory);
                const matchSearch = (!searchQuery) || 
                    v.title.toLowerCase().includes(searchQuery) || 
                    v.filename.toLowerCase().includes(searchQuery) ||
                    v.description.toLowerCase().includes(searchQuery);
                return matchCategory && matchSearch;
            }});

            sortVideos(false);
            renderVideoGrid(currentFiltered);
        }}

        function clearSearch() {{
            document.getElementById('searchInput').value = '';
            document.getElementById('clearSearchBtn').classList.add('hidden');
            searchQuery = '';
            setCategory('All');
        }}

        function sortVideos(shouldRender = true) {{
            const sortVal = document.getElementById('sortSelect').value;
            if (sortVal === 'az') {{
                currentFiltered.sort((a, b) => a.title.localeCompare(b.title));
            }} else if (sortVal === 'category') {{
                currentFiltered.sort((a, b) => a.category.localeCompare(b.category));
            }} else {{
                // Default order from drive
                currentFiltered.sort((a, b) => ALL_VIDEOS.indexOf(a) - ALL_VIDEOS.indexOf(b));
            }}
            if (shouldRender) {{
                renderVideoGrid(currentFiltered);
            }}
        }}

        // Modal / Lightbox Functions (Normal Browser Video Player)
        function openModalByIndex(index) {{
            if (!currentFiltered[index]) return;
            currentModalIndex = index;
            const video = currentFiltered[index];
            updateModalContent(video);
        }}

        function openModalById(id) {{
            const idx = currentFiltered.findIndex(v => v.id === id);
            if (idx !== -1) {{
                openModalByIndex(idx);
            }} else {{
                const rawIdx = ALL_VIDEOS.findIndex(v => v.id === id);
                if (rawIdx !== -1) {{
                    currentFiltered = [...ALL_VIDEOS];
                    openModalByIndex(rawIdx);
                }}
            }}
        }}

        function updateModalContent(video) {{
            const modal = document.getElementById('videoModal');
            const modalBox = document.getElementById('modalBox');
            const player = document.getElementById('browserVideoPlayer');
            const loader = document.getElementById('playerLoader');
            
            document.getElementById('modalTitle').innerText = video.title;
            document.getElementById('modalCategory').innerText = video.category;
            document.getElementById('modalDriveLink').href = video.driveUrl;
            document.getElementById('modalCounter').innerText = `${{currentModalIndex + 1}} / ${{currentFiltered.length}}`;

            if (loader) loader.classList.remove('hidden');

            const errorBox = document.getElementById('playerError');
            if (errorBox) errorBox.classList.add('hidden');
            const errorBtn = document.getElementById('errorDriveBtn');
            if (errorBtn) errorBtn.href = video.driveUrl;

            // Wire up event listeners
            player.oncanplay = () => {{
                if (loader) loader.classList.add('hidden');
            }};
            player.onplaying = () => {{
                if (loader) loader.classList.add('hidden');
            }};
            player.onwaiting = () => {{
                if (loader) loader.classList.remove('hidden');
            }};
            let triedFallback = false;
            player.onerror = () => {{
                if (!triedFallback) {{
                    triedFallback = true;
                    // If /video.php fails, try /api/video (for Vercel)
                    player.src = `/api/video?id=${{video.id}}`;
                    player.load();
                    player.play().catch(() => {{}});
                    return;
                }}
                if (loader) loader.classList.add('hidden');
                if (errorBox) errorBox.classList.remove('hidden');
            }};

            // Stream directly through Hostinger PHP stream or Vercel API
            player.src = `/video.php?id=${{video.id}}`;
            player.poster = video.thumbnail || video.remoteThumbnail || '';
            player.load();
            player.play().catch(() => {{
                if (loader) loader.classList.add('hidden');
            }});

            // Show modal
            modal.classList.remove('hidden');
            setTimeout(() => {{
                modal.classList.remove('opacity-0');
                modalBox.classList.remove('scale-95');
                modalBox.classList.add('scale-100');
            }}, 20);

            document.body.style.overflow = 'hidden';
            lucide.createIcons();
        }}

        function closeModal() {{
            const modal = document.getElementById('videoModal');
            const modalBox = document.getElementById('modalBox');
            const player = document.getElementById('browserVideoPlayer');

            modal.classList.add('opacity-0');
            modalBox.classList.remove('scale-100');
            modalBox.classList.add('scale-95');

            // Immediately pause and stop stream
            if (player) {{
                player.pause();
                player.removeAttribute('src');
                player.load();
            }}

            setTimeout(() => {{
                modal.classList.add('hidden');
            }}, 250);

            document.body.style.overflow = '';
        }}

        function prevVideo() {{
            if (currentModalIndex > 0) {{
                openModalByIndex(currentModalIndex - 1);
            }} else {{
                openModalByIndex(currentFiltered.length - 1);
            }}
        }}

        function nextVideo() {{
            if (currentModalIndex < currentFiltered.length - 1) {{
                openModalByIndex(currentModalIndex + 1);
            }} else {{
                openModalByIndex(0);
            }}
        }}
    </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Updated index.html: Standard browser video player configured with streaming proxy.")
