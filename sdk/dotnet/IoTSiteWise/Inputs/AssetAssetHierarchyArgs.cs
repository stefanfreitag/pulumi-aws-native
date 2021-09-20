// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTSiteWise.Inputs
{

    /// <summary>
    /// A hierarchy specifies allowed parent/child asset relationships.
    /// </summary>
    public sealed class AssetAssetHierarchyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the child asset to be associated.
        /// </summary>
        [Input("childAssetId", required: true)]
        public Input<string> ChildAssetId { get; set; } = null!;

        /// <summary>
        /// The LogicalID of a hierarchy in the parent asset's model.
        /// </summary>
        [Input("logicalId", required: true)]
        public Input<string> LogicalId { get; set; } = null!;

        public AssetAssetHierarchyArgs()
        {
        }
    }
}
