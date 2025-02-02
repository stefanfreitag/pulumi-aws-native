// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::B2BI::Transformer Resource Type
 */
export class Transformer extends pulumi.CustomResource {
    /**
     * Get an existing Transformer resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Transformer {
        return new Transformer(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:b2bi:Transformer';

    /**
     * Returns true if the given object is an instance of Transformer.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Transformer {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Transformer.__pulumiType;
    }

    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    public readonly ediType!: pulumi.Output<outputs.b2bi.TransformerEdiTypeProperties>;
    public readonly fileFormat!: pulumi.Output<enums.b2bi.TransformerFileFormat>;
    public readonly mappingTemplate!: pulumi.Output<string>;
    public readonly modifiedAt!: pulumi.Output<string | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly sampleDocument!: pulumi.Output<string | undefined>;
    public readonly status!: pulumi.Output<enums.b2bi.TransformerStatus>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    public /*out*/ readonly transformerArn!: pulumi.Output<string>;
    public /*out*/ readonly transformerId!: pulumi.Output<string>;

    /**
     * Create a Transformer resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TransformerArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.ediType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ediType'");
            }
            if ((!args || args.fileFormat === undefined) && !opts.urn) {
                throw new Error("Missing required property 'fileFormat'");
            }
            if ((!args || args.mappingTemplate === undefined) && !opts.urn) {
                throw new Error("Missing required property 'mappingTemplate'");
            }
            if ((!args || args.status === undefined) && !opts.urn) {
                throw new Error("Missing required property 'status'");
            }
            resourceInputs["ediType"] = args ? args.ediType : undefined;
            resourceInputs["fileFormat"] = args ? args.fileFormat : undefined;
            resourceInputs["mappingTemplate"] = args ? args.mappingTemplate : undefined;
            resourceInputs["modifiedAt"] = args ? args.modifiedAt : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["sampleDocument"] = args ? args.sampleDocument : undefined;
            resourceInputs["status"] = args ? args.status : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["transformerArn"] = undefined /*out*/;
            resourceInputs["transformerId"] = undefined /*out*/;
        } else {
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["ediType"] = undefined /*out*/;
            resourceInputs["fileFormat"] = undefined /*out*/;
            resourceInputs["mappingTemplate"] = undefined /*out*/;
            resourceInputs["modifiedAt"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["sampleDocument"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["transformerArn"] = undefined /*out*/;
            resourceInputs["transformerId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Transformer.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Transformer resource.
 */
export interface TransformerArgs {
    ediType: pulumi.Input<inputs.b2bi.TransformerEdiTypePropertiesArgs>;
    fileFormat: pulumi.Input<enums.b2bi.TransformerFileFormat>;
    mappingTemplate: pulumi.Input<string>;
    modifiedAt?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    sampleDocument?: pulumi.Input<string>;
    status: pulumi.Input<enums.b2bi.TransformerStatus>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
