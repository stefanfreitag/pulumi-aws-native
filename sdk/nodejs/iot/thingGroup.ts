// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::IoT::ThingGroup
 */
export class ThingGroup extends pulumi.CustomResource {
    /**
     * Get an existing ThingGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ThingGroup {
        return new ThingGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iot:ThingGroup';

    /**
     * Returns true if the given object is an instance of ThingGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ThingGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ThingGroup.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly parentGroupName!: pulumi.Output<string | undefined>;
    public readonly queryString!: pulumi.Output<string | undefined>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    public readonly thingGroupName!: pulumi.Output<string | undefined>;
    public readonly thingGroupProperties!: pulumi.Output<outputs.iot.ThingGroupPropertiesProperties | undefined>;

    /**
     * Create a ThingGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ThingGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["parentGroupName"] = args ? args.parentGroupName : undefined;
            resourceInputs["queryString"] = args ? args.queryString : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["thingGroupName"] = args ? args.thingGroupName : undefined;
            resourceInputs["thingGroupProperties"] = args ? args.thingGroupProperties : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["parentGroupName"] = undefined /*out*/;
            resourceInputs["queryString"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["thingGroupName"] = undefined /*out*/;
            resourceInputs["thingGroupProperties"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["parentGroupName", "thingGroupName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ThingGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ThingGroup resource.
 */
export interface ThingGroupArgs {
    parentGroupName?: pulumi.Input<string>;
    queryString?: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    thingGroupName?: pulumi.Input<string>;
    thingGroupProperties?: pulumi.Input<inputs.iot.ThingGroupPropertiesPropertiesArgs>;
}
