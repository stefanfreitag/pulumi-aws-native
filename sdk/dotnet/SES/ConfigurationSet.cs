// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SES
{
    /// <summary>
    /// Resource schema for AWS::SES::ConfigurationSet.
    /// </summary>
    [AwsNativeResourceType("aws-native:ses:ConfigurationSet")]
    public partial class ConfigurationSet : global::Pulumi.CustomResource
    {
        [Output("deliveryOptions")]
        public Output<Outputs.ConfigurationSetDeliveryOptions?> DeliveryOptions { get; private set; } = null!;

        /// <summary>
        /// The name of the configuration set.
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("reputationOptions")]
        public Output<Outputs.ConfigurationSetReputationOptions?> ReputationOptions { get; private set; } = null!;

        [Output("sendingOptions")]
        public Output<Outputs.ConfigurationSetSendingOptions?> SendingOptions { get; private set; } = null!;

        [Output("suppressionOptions")]
        public Output<Outputs.ConfigurationSetSuppressionOptions?> SuppressionOptions { get; private set; } = null!;

        [Output("trackingOptions")]
        public Output<Outputs.ConfigurationSetTrackingOptions?> TrackingOptions { get; private set; } = null!;


        /// <summary>
        /// Create a ConfigurationSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ConfigurationSet(string name, ConfigurationSetArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:ses:ConfigurationSet", name, args ?? new ConfigurationSetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ConfigurationSet(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ses:ConfigurationSet", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ConfigurationSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ConfigurationSet Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ConfigurationSet(name, id, options);
        }
    }

    public sealed class ConfigurationSetArgs : global::Pulumi.ResourceArgs
    {
        [Input("deliveryOptions")]
        public Input<Inputs.ConfigurationSetDeliveryOptionsArgs>? DeliveryOptions { get; set; }

        /// <summary>
        /// The name of the configuration set.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("reputationOptions")]
        public Input<Inputs.ConfigurationSetReputationOptionsArgs>? ReputationOptions { get; set; }

        [Input("sendingOptions")]
        public Input<Inputs.ConfigurationSetSendingOptionsArgs>? SendingOptions { get; set; }

        [Input("suppressionOptions")]
        public Input<Inputs.ConfigurationSetSuppressionOptionsArgs>? SuppressionOptions { get; set; }

        [Input("trackingOptions")]
        public Input<Inputs.ConfigurationSetTrackingOptionsArgs>? TrackingOptions { get; set; }

        public ConfigurationSetArgs()
        {
        }
        public static new ConfigurationSetArgs Empty => new ConfigurationSetArgs();
    }
}
