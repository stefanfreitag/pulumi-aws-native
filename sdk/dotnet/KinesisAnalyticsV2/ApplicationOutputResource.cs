// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalyticsV2
{
    /// <summary>
    /// Resource Type definition for AWS::KinesisAnalyticsV2::ApplicationOutput
    /// </summary>
    [Obsolete(@"ApplicationOutputResource is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:kinesisanalyticsv2:ApplicationOutputResource")]
    public partial class ApplicationOutputResource : global::Pulumi.CustomResource
    {
        [Output("applicationName")]
        public Output<string> ApplicationName { get; private set; } = null!;

        [Output("output")]
        public Output<Outputs.ApplicationOutputResourceOutput> Output { get; private set; } = null!;


        /// <summary>
        /// Create a ApplicationOutputResource resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ApplicationOutputResource(string name, ApplicationOutputResourceArgs args, CustomResourceOptions? options = null)
            : base("aws-native:kinesisanalyticsv2:ApplicationOutputResource", name, args ?? new ApplicationOutputResourceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ApplicationOutputResource(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:kinesisanalyticsv2:ApplicationOutputResource", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ApplicationOutputResource resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ApplicationOutputResource Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ApplicationOutputResource(name, id, options);
        }
    }

    public sealed class ApplicationOutputResourceArgs : global::Pulumi.ResourceArgs
    {
        [Input("applicationName", required: true)]
        public Input<string> ApplicationName { get; set; } = null!;

        [Input("output", required: true)]
        public Input<Inputs.ApplicationOutputResourceOutputArgs> Output { get; set; } = null!;

        public ApplicationOutputResourceArgs()
        {
        }
        public static new ApplicationOutputResourceArgs Empty => new ApplicationOutputResourceArgs();
    }
}
