// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    /// <summary>
    /// Resource schema of AWS::EC2::PrefixList Type
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:PrefixList")]
    public partial class PrefixList : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Ip Version of Prefix List.
        /// </summary>
        [Output("addressFamily")]
        public Output<Pulumi.AwsNative.Ec2.PrefixListAddressFamily> AddressFamily { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Prefix List.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Entries of Prefix List.
        /// </summary>
        [Output("entries")]
        public Output<ImmutableArray<Outputs.PrefixListEntry>> Entries { get; private set; } = null!;

        /// <summary>
        /// Max Entries of Prefix List.
        /// </summary>
        [Output("maxEntries")]
        public Output<int?> MaxEntries { get; private set; } = null!;

        /// <summary>
        /// Owner Id of Prefix List.
        /// </summary>
        [Output("ownerId")]
        public Output<string> OwnerId { get; private set; } = null!;

        /// <summary>
        /// Id of Prefix List.
        /// </summary>
        [Output("prefixListId")]
        public Output<string> PrefixListId { get; private set; } = null!;

        /// <summary>
        /// Name of Prefix List.
        /// </summary>
        [Output("prefixListName")]
        public Output<string> PrefixListName { get; private set; } = null!;

        /// <summary>
        /// Tags for Prefix List
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        /// <summary>
        /// Version of Prefix List.
        /// </summary>
        [Output("version")]
        public Output<int> Version { get; private set; } = null!;


        /// <summary>
        /// Create a PrefixList resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PrefixList(string name, PrefixListArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:PrefixList", name, args ?? new PrefixListArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PrefixList(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:PrefixList", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing PrefixList resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PrefixList Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new PrefixList(name, id, options);
        }
    }

    public sealed class PrefixListArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Ip Version of Prefix List.
        /// </summary>
        [Input("addressFamily", required: true)]
        public Input<Pulumi.AwsNative.Ec2.PrefixListAddressFamily> AddressFamily { get; set; } = null!;

        [Input("entries")]
        private InputList<Inputs.PrefixListEntryArgs>? _entries;

        /// <summary>
        /// Entries of Prefix List.
        /// </summary>
        public InputList<Inputs.PrefixListEntryArgs> Entries
        {
            get => _entries ?? (_entries = new InputList<Inputs.PrefixListEntryArgs>());
            set => _entries = value;
        }

        /// <summary>
        /// Max Entries of Prefix List.
        /// </summary>
        [Input("maxEntries")]
        public Input<int>? MaxEntries { get; set; }

        /// <summary>
        /// Name of Prefix List.
        /// </summary>
        [Input("prefixListName")]
        public Input<string>? PrefixListName { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// Tags for Prefix List
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public PrefixListArgs()
        {
        }
        public static new PrefixListArgs Empty => new PrefixListArgs();
    }
}
