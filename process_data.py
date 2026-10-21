import json

with open('videos.json', 'r', encoding='utf-8') as f:
    raw_videos = json.load(f)

# Helper function to assign clean title, category, and tags
def process_video(item):
    filename = item['title'].replace('\\u0026', '&')
    fid = item['id']
    lower = filename.lower()
    
    category = "Commercials & Ads"
    clean_title = filename.replace('.mp4', '').replace('.mov', '').strip()
    desc = "AI-crafted visual storytelling and production."

    if any(k in lower for k in ['bkc', 'finance', 'nps', 'stock', 'tariff', 'ponzi', 'sanchay', 'tatkal']):
        category = "Finance & Corporate"
        desc = "High-impact financial explainer and commercial TVC."
    elif any(k in lower for k in ['scholarship', 'berlin', 'germany', 'france', 'lithuania', 'european', 'study', 'nb ']):
        category = "Education & Global"
        desc = "Overseas education and global university recruitment campaign."
    elif any(k in lower for k in ['ruhani', 'safar', 'hanuman', 'mother', 'daughter', 'fear', 'kaamyabi']):
        category = "Narrative & Drama"
        desc = "Emotionally resonant cinematic short with rich storytelling."
    elif any(k in lower for k in ['imerbela', 'neem', 'oil', 'jeweller', 'gym', 'kisan4u', 'ads']):
        category = "Commercials & Ads"
        desc = "Brand film highlighting product benefits and visual aesthetics."
    elif any(k in lower for k in ['ai', 'promotional', 'showreel', '0507']):
        category = "AI & Showreels"
        desc = "Next-gen generative AI visuals and experimental showcases."

    # Format human-readable titles
    title_map = {
        "2nd ads update.mp4": "Digital Ad Campaign - Cut 02",
        "3 Neem Seed Kernel final video.mp4": "Neem Seed Kernel - Product Launch",
        "0507.mp4": "AI Concept Visuals 0507",
        "ai.mp4": "Cinematic AI Universe Showcase",
        "Arabic Language Neem Seed Kernel.mp4": "Neem Seed Kernel (Arabic Edition)",
        "BKC FINANCE MOVIE.mp4": "BKC Finance Short Brand Movie",
        "Bkc Tariff 500% final.mp4": "BKC 500% Tariff Explained",
        "Canada \\u0026 India Scholarship.mp4": "Canada & India Scholarship Program",
        "Canada & India Scholarship.mp4": "Canada & India Scholarship Program",
        "Dadi imerbela oil.mp4": "Dadi Ke Nuskhe - Imerbela Herbal Oil",
        "Daughter marriage-.mp4": "Daughter's Dream Wedding - Narrative Film",
        "European.mp4": "European Gateway - Study Abroad",
        "Fear final 1.mp4": "Conquering The Unknown - Cinematic Short",
        "final 1.mp4": "Brand Impact Anthem Reel",
        "Final safar Roohani 02.mp4": "Roohani Safar - Spiritual Odyssey Vol 2",
        "final video.mp4": "Creative Showreel Cut",
        "Finance PlanNing Mela 2026.mp4": "Financial Planning Mela 2026",
        "France 01.mp4": "Study in France - Global Dreams",
        "Gym oil imerbela.mp4": "Imerbela Active Gym Recovery Oil",
        "Hanuman Jayanti.mp4": "Hanuman Jayanti Devotional Film",
        "imerbela ai video.mp4": "Imerbela AI Visual Experience",
        "imerbela hair care.mp4": "Imerbela Organic Hair Care Range",
        "Imerbela Neem seed kernel range.mp4": "Neem Seed Kernel Complete Collection",
        "Imerbela New Year.mp4": "Imerbela Festive New Year Campaign",
        "Jeweller final video.mp4": "Royal Jewellery Heritage Commercial",
        "Jeweller video.mp4": "Artisan Gold & Diamond Craftsmanship",
        "Kisan4u video.mp4": "Kisan4u - Empowering Farmers with Tech",
        "Lithuania Final video.mp4": "Study in Lithuania - Complete Guide",
        "Lithuania video.mp4": "Lithuania University Life",
        "Mother Opration.mp4": "A Mother's Strength - Emotional Story",
        "Multibagger stock.mp4": "Finding Multibagger Stocks Explained",
        "Muscle pain oil.mp4": "Instant Relief Herbal Pain Oil",
        "Nakaami Se Kaamyabi Tak Ka Ruhani Safar.mp4": "Nakaami Se Kaamyabi Tak Ka Ruhani Safar",
        "NB 3rd NUMBER UPDATE.mp4": "NB Global Educational Journey",
        "NB FINAL VIDEO 02.mp4": "NB Overseas Career Anthem",
        "NB GERMANY FINAL.mp4": "Destination Germany - Study Abroad Film",
        "NB SCHOOLARSHIP01.mp4": "Global University Scholarship Drive",
        "NB STUDY IN BERLIN.mp4": "Study in Berlin Student Perspective",
        "Nb update audio.mp4": "NB Global Opportunities Showcase",
        "Neem Seed Kernel video.mp4": "Pure Neem Seed Formulation Film",
        "Neem Seed Kernel.mp4": "Neem Seed Organic Extract",
        "New Year imerbela 1.mp4": "Imerbela New Year Special Offer",
        "Nps Final 08.mp4": "National Pension System - Smart Savings",
        "NPS fINAL 12.mp4": "NPS Retirement Freedom Guide",
        "NPS final 15.mp4": "Securing Your Family's Future with NPS",
        "NPS Sanchay 03.mp4": "NPS Sanchay Wealth Growth Film",
        "NPS TATKAL 30 SEC TVC FINAL 07.mp4": "NPS Tatkal - 30s TV Commercial",
        "NPS tatkal final 01.mp4": "NPS Tatkal Rapid Onboarding",
        "NPS TATKAL VIDEO 60 Sec Final.mp4": "NPS Tatkal 60s Brand TVC",
        "Ponzi scheme video delivery 01.mp4": "Financial Scam Awareness Campaign",
        "Promotional video.mp4": "Agency Flagship Promotional Film"
    }

    display_title = title_map.get(filename, clean_title)

    return {
        "id": fid,
        "filename": filename,
        "title": display_title,
        "category": category,
        "description": desc,
        "thumbnail": f"thumbnails/{fid}.jpg",
        "remoteThumbnail": f"https://lh3.googleusercontent.com/d/{fid}=w640",
        "previewUrl": f"https://drive.google.com/file/d/{fid}/preview",
        "directStreamUrl": f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t",
        "driveUrl": f"https://drive.google.com/file/d/{fid}/view?usp=sharing",
        "downloadUrl": f"https://drive.google.com/uc?export=download&id={fid}"
    }

processed = [process_video(v) for v in raw_videos]

with open('portfolio_data.json', 'w', encoding='utf-8') as f:
    json.dump(processed, f, indent=2, ensure_ascii=False)

print(f"Processed {len(processed)} items successfully.")
