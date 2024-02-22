// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaTailor
{
    /// <summary>
    /// Definition of AWS::MediaTailor::LiveSource Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:mediatailor:LiveSource")]
    public partial class LiveSource : global::Pulumi.CustomResource
    {
        /// <summary>
        /// &lt;p&gt;The ARN of the live source.&lt;/p&gt;
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;A list of HTTP package configuration parameters for this live source.&lt;/p&gt;
        /// </summary>
        [Output("httpPackageConfigurations")]
        public Output<ImmutableArray<Outputs.LiveSourceHttpPackageConfiguration>> HttpPackageConfigurations { get; private set; } = null!;

        [Output("liveSourceName")]
        public Output<string> LiveSourceName { get; private set; } = null!;

        [Output("sourceLocationName")]
        public Output<string> SourceLocationName { get; private set; } = null!;

        /// <summary>
        /// The tags to assign to the live source.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a LiveSource resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LiveSource(string name, LiveSourceArgs args, CustomResourceOptions? options = null)
            : base("aws-native:mediatailor:LiveSource", name, args ?? new LiveSourceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LiveSource(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:mediatailor:LiveSource", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "liveSourceName",
                    "sourceLocationName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing LiveSource resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LiveSource Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new LiveSource(name, id, options);
        }
    }

    public sealed class LiveSourceArgs : global::Pulumi.ResourceArgs
    {
        [Input("httpPackageConfigurations", required: true)]
        private InputList<Inputs.LiveSourceHttpPackageConfigurationArgs>? _httpPackageConfigurations;

        /// <summary>
        /// &lt;p&gt;A list of HTTP package configuration parameters for this live source.&lt;/p&gt;
        /// </summary>
        public InputList<Inputs.LiveSourceHttpPackageConfigurationArgs> HttpPackageConfigurations
        {
            get => _httpPackageConfigurations ?? (_httpPackageConfigurations = new InputList<Inputs.LiveSourceHttpPackageConfigurationArgs>());
            set => _httpPackageConfigurations = value;
        }

        [Input("liveSourceName")]
        public Input<string>? LiveSourceName { get; set; }

        [Input("sourceLocationName", required: true)]
        public Input<string> SourceLocationName { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// The tags to assign to the live source.
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public LiveSourceArgs()
        {
        }
        public static new LiveSourceArgs Empty => new LiveSourceArgs();
    }
}
