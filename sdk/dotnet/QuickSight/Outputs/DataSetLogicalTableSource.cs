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
    /// &lt;p&gt;Information about the source of a logical table. This is a variant type structure. For
    ///             this structure to be valid, only one of the attributes can be non-null.&lt;/p&gt;
    /// </summary>
    [OutputType]
    public sealed class DataSetLogicalTableSource
    {
        /// <summary>
        /// &lt;p&gt;The Amazon Resource Name (ARN) for the dataset.&lt;/p&gt;
        /// </summary>
        public readonly string? DataSetArn;
        public readonly Outputs.DataSetJoinInstruction? JoinInstruction;
        /// <summary>
        /// &lt;p&gt;Physical table ID.&lt;/p&gt;
        /// </summary>
        public readonly string? PhysicalTableId;

        [OutputConstructor]
        private DataSetLogicalTableSource(
            string? dataSetArn,

            Outputs.DataSetJoinInstruction? joinInstruction,

            string? physicalTableId)
        {
            DataSetArn = dataSetArn;
            JoinInstruction = joinInstruction;
            PhysicalTableId = physicalTableId;
        }
    }
}
