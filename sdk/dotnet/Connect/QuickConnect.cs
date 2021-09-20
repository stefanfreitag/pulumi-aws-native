// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect
{
    /// <summary>
    /// Resource Type definition for AWS::Connect::QuickConnect
    /// </summary>
    [AwsNativeResourceType("aws-native:connect:QuickConnect")]
    public partial class QuickConnect : Pulumi.CustomResource
    {
        /// <summary>
        /// The description of the quick connect.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The identifier of the Amazon Connect instance.
        /// </summary>
        [Output("instanceArn")]
        public Output<string> InstanceArn { get; private set; } = null!;

        /// <summary>
        /// The name of the quick connect.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) for the quick connect.
        /// </summary>
        [Output("quickConnectArn")]
        public Output<string> QuickConnectArn { get; private set; } = null!;

        /// <summary>
        /// Configuration settings for the quick connect.
        /// </summary>
        [Output("quickConnectConfig")]
        public Output<Outputs.QuickConnectQuickConnectConfig> QuickConnectConfig { get; private set; } = null!;

        /// <summary>
        /// One or more tags.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.QuickConnectTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a QuickConnect resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public QuickConnect(string name, QuickConnectArgs args, CustomResourceOptions? options = null)
            : base("aws-native:connect:QuickConnect", name, args ?? new QuickConnectArgs(), MakeResourceOptions(options, ""))
        {
        }

        private QuickConnect(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:connect:QuickConnect", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing QuickConnect resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static QuickConnect Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new QuickConnect(name, id, options);
        }
    }

    public sealed class QuickConnectArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the quick connect.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The identifier of the Amazon Connect instance.
        /// </summary>
        [Input("instanceArn", required: true)]
        public Input<string> InstanceArn { get; set; } = null!;

        /// <summary>
        /// The name of the quick connect.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// Configuration settings for the quick connect.
        /// </summary>
        [Input("quickConnectConfig", required: true)]
        public Input<Inputs.QuickConnectQuickConnectConfigArgs> QuickConnectConfig { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.QuickConnectTagArgs>? _tags;

        /// <summary>
        /// One or more tags.
        /// </summary>
        public InputList<Inputs.QuickConnectTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.QuickConnectTagArgs>());
            set => _tags = value;
        }

        public QuickConnectArgs()
        {
        }
    }
}
