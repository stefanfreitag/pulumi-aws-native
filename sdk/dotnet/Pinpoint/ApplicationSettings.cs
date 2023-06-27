// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pinpoint
{
    /// <summary>
    /// Resource Type definition for AWS::Pinpoint::ApplicationSettings
    /// </summary>
    [Obsolete(@"ApplicationSettings is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:pinpoint:ApplicationSettings")]
    public partial class ApplicationSettings : global::Pulumi.CustomResource
    {
        [Output("applicationId")]
        public Output<string> ApplicationId { get; private set; } = null!;

        [Output("campaignHook")]
        public Output<Outputs.ApplicationSettingsCampaignHook?> CampaignHook { get; private set; } = null!;

        [Output("cloudWatchMetricsEnabled")]
        public Output<bool?> CloudWatchMetricsEnabled { get; private set; } = null!;

        [Output("limits")]
        public Output<Outputs.ApplicationSettingsLimits?> Limits { get; private set; } = null!;

        [Output("quietTime")]
        public Output<Outputs.ApplicationSettingsQuietTime?> QuietTime { get; private set; } = null!;


        /// <summary>
        /// Create a ApplicationSettings resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ApplicationSettings(string name, ApplicationSettingsArgs args, CustomResourceOptions? options = null)
            : base("aws-native:pinpoint:ApplicationSettings", name, args ?? new ApplicationSettingsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ApplicationSettings(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:pinpoint:ApplicationSettings", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ApplicationSettings resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ApplicationSettings Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ApplicationSettings(name, id, options);
        }
    }

    public sealed class ApplicationSettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("applicationId", required: true)]
        public Input<string> ApplicationId { get; set; } = null!;

        [Input("campaignHook")]
        public Input<Inputs.ApplicationSettingsCampaignHookArgs>? CampaignHook { get; set; }

        [Input("cloudWatchMetricsEnabled")]
        public Input<bool>? CloudWatchMetricsEnabled { get; set; }

        [Input("limits")]
        public Input<Inputs.ApplicationSettingsLimitsArgs>? Limits { get; set; }

        [Input("quietTime")]
        public Input<Inputs.ApplicationSettingsQuietTimeArgs>? QuietTime { get; set; }

        public ApplicationSettingsArgs()
        {
        }
        public static new ApplicationSettingsArgs Empty => new ApplicationSettingsArgs();
    }
}
