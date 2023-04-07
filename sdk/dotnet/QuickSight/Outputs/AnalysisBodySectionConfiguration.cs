// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class AnalysisBodySectionConfiguration
    {
        public readonly Outputs.AnalysisBodySectionContent Content;
        public readonly Outputs.AnalysisSectionPageBreakConfiguration? PageBreakConfiguration;
        public readonly string SectionId;
        public readonly Outputs.AnalysisSectionStyle? Style;

        [OutputConstructor]
        private AnalysisBodySectionConfiguration(
            Outputs.AnalysisBodySectionContent content,

            Outputs.AnalysisSectionPageBreakConfiguration? pageBreakConfiguration,

            string sectionId,

            Outputs.AnalysisSectionStyle? style)
        {
            Content = content;
            PageBreakConfiguration = pageBreakConfiguration;
            SectionId = sectionId;
            Style = style;
        }
    }
}
