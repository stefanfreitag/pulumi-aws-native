// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GuardDuty
{
    /// <summary>
    /// Resource Type definition for AWS::GuardDuty::ThreatIntelSet
    /// </summary>
    [Obsolete(@"ThreatIntelSet is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:guardduty:ThreatIntelSet")]
    public partial class ThreatIntelSet : Pulumi.CustomResource
    {
        [Output("activate")]
        public Output<bool> Activate { get; private set; } = null!;

        [Output("detectorId")]
        public Output<string> DetectorId { get; private set; } = null!;

        [Output("format")]
        public Output<string> Format { get; private set; } = null!;

        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;


        /// <summary>
        /// Create a ThreatIntelSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ThreatIntelSet(string name, ThreatIntelSetArgs args, CustomResourceOptions? options = null)
            : base("aws-native:guardduty:ThreatIntelSet", name, args ?? new ThreatIntelSetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ThreatIntelSet(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:guardduty:ThreatIntelSet", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ThreatIntelSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ThreatIntelSet Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ThreatIntelSet(name, id, options);
        }
    }

    public sealed class ThreatIntelSetArgs : Pulumi.ResourceArgs
    {
        [Input("activate", required: true)]
        public Input<bool> Activate { get; set; } = null!;

        [Input("detectorId", required: true)]
        public Input<string> DetectorId { get; set; } = null!;

        [Input("format", required: true)]
        public Input<string> Format { get; set; } = null!;

        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        public ThreatIntelSetArgs()
        {
        }
    }
}
