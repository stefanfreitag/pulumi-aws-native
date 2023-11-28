// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::IoTTwinMaker::Entity
 */
export class Entity extends pulumi.CustomResource {
    /**
     * Get an existing Entity resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Entity {
        return new Entity(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iottwinmaker:Entity';

    /**
     * Returns true if the given object is an instance of Entity.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Entity {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Entity.__pulumiType;
    }

    /**
     * The ARN of the entity.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * A map that sets information about a component type.
     */
    public readonly components!: pulumi.Output<any | undefined>;
    /**
     * A map that sets information about a composite component.
     */
    public readonly compositeComponents!: pulumi.Output<any | undefined>;
    /**
     * The date and time when the entity was created.
     */
    public /*out*/ readonly creationDateTime!: pulumi.Output<string>;
    /**
     * The description of the entity.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The ID of the entity.
     */
    public readonly entityId!: pulumi.Output<string | undefined>;
    /**
     * The name of the entity.
     */
    public readonly entityName!: pulumi.Output<string>;
    /**
     * A Boolean value that specifies whether the entity has child entities or not.
     */
    public /*out*/ readonly hasChildEntities!: pulumi.Output<boolean>;
    /**
     * The ID of the parent entity.
     */
    public readonly parentEntityId!: pulumi.Output<string | undefined>;
    /**
     * The current status of the entity.
     */
    public /*out*/ readonly status!: pulumi.Output<outputs.iottwinmaker.EntityStatus>;
    /**
     * A key-value pair to associate with a resource.
     */
    public readonly tags!: pulumi.Output<any | undefined>;
    /**
     * The last date and time when the entity was updated.
     */
    public /*out*/ readonly updateDateTime!: pulumi.Output<string>;
    /**
     * The ID of the workspace.
     */
    public readonly workspaceId!: pulumi.Output<string>;

    /**
     * Create a Entity resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: EntityArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.workspaceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'workspaceId'");
            }
            resourceInputs["components"] = args ? args.components : undefined;
            resourceInputs["compositeComponents"] = args ? args.compositeComponents : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["entityId"] = args ? args.entityId : undefined;
            resourceInputs["entityName"] = args ? args.entityName : undefined;
            resourceInputs["parentEntityId"] = args ? args.parentEntityId : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["workspaceId"] = args ? args.workspaceId : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["creationDateTime"] = undefined /*out*/;
            resourceInputs["hasChildEntities"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["updateDateTime"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["components"] = undefined /*out*/;
            resourceInputs["compositeComponents"] = undefined /*out*/;
            resourceInputs["creationDateTime"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["entityId"] = undefined /*out*/;
            resourceInputs["entityName"] = undefined /*out*/;
            resourceInputs["hasChildEntities"] = undefined /*out*/;
            resourceInputs["parentEntityId"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["updateDateTime"] = undefined /*out*/;
            resourceInputs["workspaceId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["entityId", "workspaceId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Entity.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Entity resource.
 */
export interface EntityArgs {
    /**
     * A map that sets information about a component type.
     */
    components?: any;
    /**
     * A map that sets information about a composite component.
     */
    compositeComponents?: any;
    /**
     * The description of the entity.
     */
    description?: pulumi.Input<string>;
    /**
     * The ID of the entity.
     */
    entityId?: pulumi.Input<string>;
    /**
     * The name of the entity.
     */
    entityName?: pulumi.Input<string>;
    /**
     * The ID of the parent entity.
     */
    parentEntityId?: pulumi.Input<string>;
    /**
     * A key-value pair to associate with a resource.
     */
    tags?: any;
    /**
     * The ID of the workspace.
     */
    workspaceId: pulumi.Input<string>;
}
