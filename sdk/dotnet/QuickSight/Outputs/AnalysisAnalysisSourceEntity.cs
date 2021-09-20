// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    /// <summary>
    /// &lt;p&gt;The source entity of an analysis.&lt;/p&gt;
    /// </summary>
    [OutputType]
    public sealed class AnalysisAnalysisSourceEntity
    {
        public readonly Outputs.AnalysisAnalysisSourceTemplate? SourceTemplate;

        [OutputConstructor]
        private AnalysisAnalysisSourceEntity(Outputs.AnalysisAnalysisSourceTemplate? sourceTemplate)
        {
            SourceTemplate = sourceTemplate;
        }
    }
}
