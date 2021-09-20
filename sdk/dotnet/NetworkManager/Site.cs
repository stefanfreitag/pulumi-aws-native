// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NetworkManager
{
    /// <summary>
    /// The AWS::NetworkManager::Site type describes a site.
    /// </summary>
    [AwsNativeResourceType("aws-native:networkmanager:Site")]
    public partial class Site : Pulumi.CustomResource
    {
        /// <summary>
        /// The description of the site.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The ID of the global network.
        /// </summary>
        [Output("globalNetworkId")]
        public Output<string> GlobalNetworkId { get; private set; } = null!;

        /// <summary>
        /// The location of the site.
        /// </summary>
        [Output("location")]
        public Output<Outputs.SiteLocation?> Location { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the site.
        /// </summary>
        [Output("siteArn")]
        public Output<string> SiteArn { get; private set; } = null!;

        /// <summary>
        /// The ID of the site.
        /// </summary>
        [Output("siteId")]
        public Output<string> SiteId { get; private set; } = null!;

        /// <summary>
        /// The tags for the site.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.SiteTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Site resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Site(string name, SiteArgs args, CustomResourceOptions? options = null)
            : base("aws-native:networkmanager:Site", name, args ?? new SiteArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Site(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:networkmanager:Site", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Site resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Site Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Site(name, id, options);
        }
    }

    public sealed class SiteArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the site.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The ID of the global network.
        /// </summary>
        [Input("globalNetworkId", required: true)]
        public Input<string> GlobalNetworkId { get; set; } = null!;

        /// <summary>
        /// The location of the site.
        /// </summary>
        [Input("location")]
        public Input<Inputs.SiteLocationArgs>? Location { get; set; }

        [Input("tags")]
        private InputList<Inputs.SiteTagArgs>? _tags;

        /// <summary>
        /// The tags for the site.
        /// </summary>
        public InputList<Inputs.SiteTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.SiteTagArgs>());
            set => _tags = value;
        }

        public SiteArgs()
        {
        }
    }
}
