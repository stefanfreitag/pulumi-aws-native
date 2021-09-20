// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DevOpsGuru
{
    /// <summary>
    /// This resource schema represents the NotificationChannel resource in the Amazon DevOps Guru.
    /// </summary>
    [AwsNativeResourceType("aws-native:devopsguru:NotificationChannel")]
    public partial class NotificationChannel : Pulumi.CustomResource
    {
        [Output("config")]
        public Output<Outputs.NotificationChannelNotificationChannelConfig> Config { get; private set; } = null!;


        /// <summary>
        /// Create a NotificationChannel resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NotificationChannel(string name, NotificationChannelArgs args, CustomResourceOptions? options = null)
            : base("aws-native:devopsguru:NotificationChannel", name, args ?? new NotificationChannelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NotificationChannel(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:devopsguru:NotificationChannel", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing NotificationChannel resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NotificationChannel Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new NotificationChannel(name, id, options);
        }
    }

    public sealed class NotificationChannelArgs : Pulumi.ResourceArgs
    {
        [Input("config", required: true)]
        public Input<Inputs.NotificationChannelNotificationChannelConfigArgs> Config { get; set; } = null!;

        public NotificationChannelArgs()
        {
        }
    }
}
