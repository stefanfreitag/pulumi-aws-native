// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ResourceExplorer2
{
    /// <summary>
    /// Definition of AWS::ResourceExplorer2::DefaultViewAssociation Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:resourceexplorer2:DefaultViewAssociation")]
    public partial class DefaultViewAssociation : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The AWS principal that the default view is associated with, used as the unique identifier for this resource.
        /// </summary>
        [Output("associatedAwsPrincipal")]
        public Output<string> AssociatedAwsPrincipal { get; private set; } = null!;

        [Output("viewArn")]
        public Output<string> ViewArn { get; private set; } = null!;


        /// <summary>
        /// Create a DefaultViewAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DefaultViewAssociation(string name, DefaultViewAssociationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:resourceexplorer2:DefaultViewAssociation", name, args ?? new DefaultViewAssociationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DefaultViewAssociation(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:resourceexplorer2:DefaultViewAssociation", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing DefaultViewAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DefaultViewAssociation Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DefaultViewAssociation(name, id, options);
        }
    }

    public sealed class DefaultViewAssociationArgs : global::Pulumi.ResourceArgs
    {
        [Input("viewArn", required: true)]
        public Input<string> ViewArn { get; set; } = null!;

        public DefaultViewAssociationArgs()
        {
        }
        public static new DefaultViewAssociationArgs Empty => new DefaultViewAssociationArgs();
    }
}
