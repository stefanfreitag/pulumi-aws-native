// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTTwinMaker
{
    /// <summary>
    /// Resource schema for AWS::IoTTwinMaker::Entity
    /// </summary>
    [AwsNativeResourceType("aws-native:iottwinmaker:Entity")]
    public partial class Entity : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the entity.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// A map that sets information about a component type.
        /// </summary>
        [Output("components")]
        public Output<object?> Components { get; private set; } = null!;

        /// <summary>
        /// A map that sets information about a composite component.
        /// </summary>
        [Output("compositeComponents")]
        public Output<object?> CompositeComponents { get; private set; } = null!;

        /// <summary>
        /// The date and time when the entity was created.
        /// </summary>
        [Output("creationDateTime")]
        public Output<string> CreationDateTime { get; private set; } = null!;

        /// <summary>
        /// The description of the entity.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The ID of the entity.
        /// </summary>
        [Output("entityId")]
        public Output<string?> EntityId { get; private set; } = null!;

        /// <summary>
        /// The name of the entity.
        /// </summary>
        [Output("entityName")]
        public Output<string> EntityName { get; private set; } = null!;

        /// <summary>
        /// A Boolean value that specifies whether the entity has child entities or not.
        /// </summary>
        [Output("hasChildEntities")]
        public Output<bool> HasChildEntities { get; private set; } = null!;

        /// <summary>
        /// The ID of the parent entity.
        /// </summary>
        [Output("parentEntityId")]
        public Output<string?> ParentEntityId { get; private set; } = null!;

        /// <summary>
        /// The current status of the entity.
        /// </summary>
        [Output("status")]
        public Output<Outputs.EntityStatus> Status { get; private set; } = null!;

        /// <summary>
        /// A key-value pair to associate with a resource.
        /// </summary>
        [Output("tags")]
        public Output<object?> Tags { get; private set; } = null!;

        /// <summary>
        /// The last date and time when the entity was updated.
        /// </summary>
        [Output("updateDateTime")]
        public Output<string> UpdateDateTime { get; private set; } = null!;

        /// <summary>
        /// The ID of the workspace.
        /// </summary>
        [Output("workspaceId")]
        public Output<string> WorkspaceId { get; private set; } = null!;


        /// <summary>
        /// Create a Entity resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Entity(string name, EntityArgs args, CustomResourceOptions? options = null)
            : base("aws-native:iottwinmaker:Entity", name, args ?? new EntityArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Entity(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iottwinmaker:Entity", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "entityId",
                    "workspaceId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Entity resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Entity Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Entity(name, id, options);
        }
    }

    public sealed class EntityArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A map that sets information about a component type.
        /// </summary>
        [Input("components")]
        public Input<object>? Components { get; set; }

        /// <summary>
        /// A map that sets information about a composite component.
        /// </summary>
        [Input("compositeComponents")]
        public Input<object>? CompositeComponents { get; set; }

        /// <summary>
        /// The description of the entity.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The ID of the entity.
        /// </summary>
        [Input("entityId")]
        public Input<string>? EntityId { get; set; }

        /// <summary>
        /// The name of the entity.
        /// </summary>
        [Input("entityName")]
        public Input<string>? EntityName { get; set; }

        /// <summary>
        /// The ID of the parent entity.
        /// </summary>
        [Input("parentEntityId")]
        public Input<string>? ParentEntityId { get; set; }

        /// <summary>
        /// A key-value pair to associate with a resource.
        /// </summary>
        [Input("tags")]
        public Input<object>? Tags { get; set; }

        /// <summary>
        /// The ID of the workspace.
        /// </summary>
        [Input("workspaceId", required: true)]
        public Input<string> WorkspaceId { get; set; } = null!;

        public EntityArgs()
        {
        }
        public static new EntityArgs Empty => new EntityArgs();
    }
}
