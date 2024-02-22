// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::FSx::Volume
 *
 * @deprecated Volume is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Volume extends pulumi.CustomResource {
    /**
     * Get an existing Volume resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Volume {
        pulumi.log.warn("Volume is deprecated: Volume is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Volume(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:fsx:Volume';

    /**
     * Returns true if the given object is an instance of Volume.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Volume {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Volume.__pulumiType;
    }

    public readonly backupId!: pulumi.Output<string | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly ontapConfiguration!: pulumi.Output<outputs.fsx.VolumeOntapConfiguration | undefined>;
    public readonly openZfsConfiguration!: pulumi.Output<outputs.fsx.VolumeOpenZfsConfiguration | undefined>;
    public /*out*/ readonly resourceArn!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    public /*out*/ readonly uuid!: pulumi.Output<string>;
    public /*out*/ readonly volumeId!: pulumi.Output<string>;
    public readonly volumeType!: pulumi.Output<string | undefined>;

    /**
     * Create a Volume resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Volume is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args?: VolumeArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Volume is deprecated: Volume is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["backupId"] = args ? args.backupId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["ontapConfiguration"] = args ? args.ontapConfiguration : undefined;
            resourceInputs["openZfsConfiguration"] = args ? args.openZfsConfiguration : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["volumeType"] = args ? args.volumeType : undefined;
            resourceInputs["resourceArn"] = undefined /*out*/;
            resourceInputs["uuid"] = undefined /*out*/;
            resourceInputs["volumeId"] = undefined /*out*/;
        } else {
            resourceInputs["backupId"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["ontapConfiguration"] = undefined /*out*/;
            resourceInputs["openZfsConfiguration"] = undefined /*out*/;
            resourceInputs["resourceArn"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["uuid"] = undefined /*out*/;
            resourceInputs["volumeId"] = undefined /*out*/;
            resourceInputs["volumeType"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["backupId", "volumeType"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Volume.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Volume resource.
 */
export interface VolumeArgs {
    backupId?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    ontapConfiguration?: pulumi.Input<inputs.fsx.VolumeOntapConfigurationArgs>;
    openZfsConfiguration?: pulumi.Input<inputs.fsx.VolumeOpenZfsConfigurationArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    volumeType?: pulumi.Input<string>;
}
