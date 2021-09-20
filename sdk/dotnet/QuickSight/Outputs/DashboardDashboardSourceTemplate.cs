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
    /// &lt;p&gt;Dashboard source template.&lt;/p&gt;
    /// </summary>
    [OutputType]
    public sealed class DashboardDashboardSourceTemplate
    {
        /// <summary>
        /// &lt;p&gt;The Amazon Resource Name (ARN) of the resource.&lt;/p&gt;
        /// </summary>
        public readonly string Arn;
        /// <summary>
        /// &lt;p&gt;Dataset references.&lt;/p&gt;
        /// </summary>
        public readonly ImmutableArray<Outputs.DashboardDataSetReference> DataSetReferences;

        [OutputConstructor]
        private DashboardDashboardSourceTemplate(
            string arn,

            ImmutableArray<Outputs.DashboardDataSetReference> dataSetReferences)
        {
            Arn = arn;
            DataSetReferences = dataSetReferences;
        }
    }
}
