def format_summary_stats(stats):
    """
    Format summary statistics for display.
    
    Args:
        stats (dict): Dictionary of summary statistics
        
    Returns:
        str: Formatted string of statistics
    """
    output = []
    output.append("=== University Dataset Summary ===")
    output.append(f"Total Universities: {stats['total_universities']}")
    
    output.append("\nUniversities by Country:")
    for country, count in stats['universities_by_country'].items():
        output.append(f"  {country}: {count}")
    
    output.append(f"\nAverage Statistics:")
    output.append(f"  Students per University: {stats['avg_students']:,.0f}")
    output.append(f"  Student-to-Faculty Ratio: {stats['avg_student_faculty_ratio']:.2f}")
    output.append(f"  International Students: {stats['avg_international_students']:.1f}%")
    
    output.append("\nTop 10 Universities:")
    for uni in stats['top_10_universities']:
        output.append(f"  {uni['University Name']} (Rank: {uni['World Rank']}, {uni['Country']})")
    
    return "\n".join(output)