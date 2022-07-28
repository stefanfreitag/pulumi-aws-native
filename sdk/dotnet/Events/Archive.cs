// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Events
{
    /// <summary>
    /// Resource Type definition for AWS::Events::Archive
    /// </summary>
    [AwsNativeResourceType("aws-native:events:Archive")]
    public partial class Archive : global::Pulumi.CustomResource
    {
        [Output("archiveName")]
        public Output<string> ArchiveName { get; private set; } = null!;

        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("eventPattern")]
        public Output<object?> EventPattern { get; private set; } = null!;

        [Output("retentionDays")]
        public Output<int?> RetentionDays { get; private set; } = null!;

        [Output("sourceArn")]
        public Output<string> SourceArn { get; private set; } = null!;


        /// <summary>
        /// Create a Archive resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Archive(string name, ArchiveArgs args, CustomResourceOptions? options = null)
            : base("aws-native:events:Archive", name, args ?? new ArchiveArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Archive(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:events:Archive", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Archive resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Archive Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Archive(name, id, options);
        }
    }

    public sealed class ArchiveArgs : global::Pulumi.ResourceArgs
    {
        [Input("archiveName")]
        public Input<string>? ArchiveName { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("eventPattern")]
        public Input<object>? EventPattern { get; set; }

        [Input("retentionDays")]
        public Input<int>? RetentionDays { get; set; }

        [Input("sourceArn", required: true)]
        public Input<string> SourceArn { get; set; } = null!;

        public ArchiveArgs()
        {
        }
        public static new ArchiveArgs Empty => new ArchiveArgs();
    }
}
