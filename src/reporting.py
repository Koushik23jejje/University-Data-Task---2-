"""Module for generating analysis reports."""

def create_summary_report(stats, top_unis):
    """Create a formatted summary report."""
    lines = ["=== University Dataset Summary ==="]
    
    # Basic stats
    lines.append(f"\nTotal Universities: {stats['total_universities']}")
    
    # Country distribution
    lines.append("\nUniversities by Country:")
    for country, count in stats['universities_by_country'].items():
        lines.append(f"  {country}: {count}")
    
    # Averages
    lines.append(f"\nAverage Statistics:")
    lines.append(f"  Students per University: {stats['avg_students']:,.0f}")
    lines.append(f"  Student-to-Faculty Ratio: {stats['avg_student_faculty_ratio']:.2f}")
    lines.append(f"  International Students: {stats['avg_international_students']:.1f}%")
    
    # Top universities
    lines.append("\nTop Universities:")
    for uni in top_unis:
        lines.append(f"  {uni['University Name']} (Rank: {uni['World Rank']}, {uni['Country']})")
    
    return "\n".join(lines)