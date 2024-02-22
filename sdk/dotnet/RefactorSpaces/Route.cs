// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RefactorSpaces
{
    /// <summary>
    /// Definition of AWS::RefactorSpaces::Route Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:refactorspaces:Route")]
    public partial class Route : global::Pulumi.CustomResource
    {
        [Output("applicationIdentifier")]
        public Output<string> ApplicationIdentifier { get; private set; } = null!;

        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("defaultRoute")]
        public Output<Outputs.RouteDefaultRouteInput?> DefaultRoute { get; private set; } = null!;

        [Output("environmentIdentifier")]
        public Output<string> EnvironmentIdentifier { get; private set; } = null!;

        [Output("pathResourceToId")]
        public Output<string> PathResourceToId { get; private set; } = null!;

        [Output("routeIdentifier")]
        public Output<string> RouteIdentifier { get; private set; } = null!;

        [Output("routeType")]
        public Output<Pulumi.AwsNative.RefactorSpaces.RouteType> RouteType { get; private set; } = null!;

        [Output("serviceIdentifier")]
        public Output<string> ServiceIdentifier { get; private set; } = null!;

        /// <summary>
        /// Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        [Output("uriPathRoute")]
        public Output<Outputs.RouteUriPathRouteInput?> UriPathRoute { get; private set; } = null!;


        /// <summary>
        /// Create a Route resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Route(string name, RouteArgs args, CustomResourceOptions? options = null)
            : base("aws-native:refactorspaces:Route", name, args ?? new RouteArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Route(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:refactorspaces:Route", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "applicationIdentifier",
                    "environmentIdentifier",
                    "routeType",
                    "serviceIdentifier",
                    "uriPathRoute.appendSourcePath",
                    "uriPathRoute.includeChildPaths",
                    "uriPathRoute.methods[*]",
                    "uriPathRoute.sourcePath",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Route resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Route Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Route(name, id, options);
        }
    }

    public sealed class RouteArgs : global::Pulumi.ResourceArgs
    {
        [Input("applicationIdentifier", required: true)]
        public Input<string> ApplicationIdentifier { get; set; } = null!;

        [Input("defaultRoute")]
        public Input<Inputs.RouteDefaultRouteInputArgs>? DefaultRoute { get; set; }

        [Input("environmentIdentifier", required: true)]
        public Input<string> EnvironmentIdentifier { get; set; } = null!;

        [Input("routeType", required: true)]
        public Input<Pulumi.AwsNative.RefactorSpaces.RouteType> RouteType { get; set; } = null!;

        [Input("serviceIdentifier", required: true)]
        public Input<string> ServiceIdentifier { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        [Input("uriPathRoute")]
        public Input<Inputs.RouteUriPathRouteInputArgs>? UriPathRoute { get; set; }

        public RouteArgs()
        {
        }
        public static new RouteArgs Empty => new RouteArgs();
    }
}
